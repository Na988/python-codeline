import paramiko

def ssh_connect(host, username, password):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the host
        ssh.connect(hostname=host, username=username, password=password)
        
        print(f"Successfully connected to {host}")
        
        # Close the connection
        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {host}: {e}")

ssh_connect("192.168.100.164", "vboxuser", "Codeline")