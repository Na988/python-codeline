import os
from datetime import date
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

def get_hostname(connection, device_type):
    if device_type == 'cisco_ios':
        output = connection.send_command('show run | include hostname')
        # Output like: hostname router1
        parts = output.strip().split()
        if len(parts) >= 2:
            return parts[1]
    elif device_type == 'juniper_junos':
        output = connection.send_command('show configuration system host-name')
        # Assuming it returns the hostname
        return output.strip()
    # Add more device types as needed
    return "unknown"

def backup_config(device):
    ip = device['ip']
    device_type = device['device_type']
    username = device['username']
    password = device['password']

    print(f"Attempting to connect to {ip} ({device_type})...")

    connection = None
    try:
        connection = ConnectHandler(
            device_type=device_type,
            host=ip,
            username=username,
            password=password,
            timeout=10
        )
        print(f"Successfully connected to {ip}.")

        hostname = get_hostname(connection, device_type)
        print(f"Device Hostname: {hostname}")

        print(f"Retrieving running configuration from {hostname}...")

        if device_type == 'cisco_ios':
            config = connection.send_command('show running-config')
        elif device_type == 'juniper_junos':
            config = connection.send_command('show configuration')
        else:
            config = "Unsupported device type"

        # Create backups directory if not exists
        backup_dir = './backups'
        os.makedirs(backup_dir, exist_ok=True)

        # Current date
        today = date.today().isoformat()

        # Filename
        filename = f"{hostname}_{today}.txt"
        filepath = os.path.join(backup_dir, filename)

        # Write to file
        with open(filepath, 'w') as f:
            f.write(config)

        print(f"Configuration backup for {hostname} saved to {filepath} successfully.")

    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(f"Error backing up configuration for {ip}: {str(e)}")
    except Exception as e:
        print(f"Unexpected error for {ip}: {str(e)}")
    finally:
        if connection:
            connection.disconnect()
            print(f"Disconnected from {ip}.")
        else:
            print(f"Disconnected from {ip}.")

def main():
    # Sample device list
    devices = [
        {
            'device_type': 'cisco_ios',
            'ip': '192.168.1.1',
            'username': 'admin',
            'password': 'password'
        },
        {
            'device_type': 'cisco_ios',
            'ip': '192.168.1.2',
            'username': 'admin',
            'password': 'password'
        },
        {
            'device_type': 'cisco_ios',
            'ip': '10.0.0.1',
            'username': 'admin',
            'password': 'password'
        },
        {
            'device_type': 'juniper_junos',
            'ip': '192.168.1.3',
            'username': 'admin',
            'password': 'password'
        }
    ]

    for device in devices:
        backup_config(device)
        print()  # Blank line between devices

if __name__ == "__main__":
    main()
