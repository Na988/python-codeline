import csv
import json
from collections import Counter

def parse_log_line(line):
    parts = line.strip().split()
    if len(parts) < 8:
        return None
    try:
        timestamp = f"{parts[0]} {parts[1]}"
        action = parts[2]
        protocol = parts[3]
        if action not in ['ACCEPT', 'DROP'] or protocol not in ['TCP', 'UDP', 'ICMP']:
            return None
        # Parse key=value pairs
        data = {}
        for part in parts[4:]:
            if '=' in part:
                key, value = part.split('=', 1)
                data[key] = value
        required_keys = ['SRC', 'SPT', 'DST', 'DPT', 'LEN']
        if not all(key in data for key in required_keys):
            return None
        return {
            'timestamp': timestamp,
            'action': action,
            'protocol': protocol,
            'source_ip': data['SRC'],
            'source_port': data['SPT'],
            'destination_ip': data['DST'],
            'destination_port': data['DPT'],
            'packet_size': data['LEN']
        }
    except (ValueError, IndexError):
        return None

def main():
    log_file = 'firewall.log'
    csv_file = 'output.csv'
    json_file = 'output.json'
    threats_file = 'threats.txt'

    entries = []
    total_entries = 0
    malformed = 0
    last_timestamp = None

    # Read and parse log file
    try:
        with open(log_file, 'r') as f:
            for line in f:
                total_entries += 1
                parsed = parse_log_line(line)
                if parsed:
                    entries.append(parsed)
                    last_timestamp = parsed['timestamp']
                else:
                    malformed += 1
    except FileNotFoundError:
        print(f"Error: {log_file} not found.")
        return

    valid_entries = len(entries)

    # Analysis
    actions = Counter(entry['action'] for entry in entries)
    dest_ports = Counter(entry['destination_port'] for entry in entries)
    src_ips = Counter(entry['source_ip'] for entry in entries)

    top_ports = dest_ports.most_common(3)
    suspicious_ips = {ip: count for ip, count in src_ips.items() if count >= 3}

    # Save to CSV
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Timestamp', 'Action', 'Protocol', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Packet Size'])
        writer.writeheader()
        for entry in entries:
            writer.writerow({
                'Timestamp': entry['timestamp'],
                'Action': entry['action'],
                'Protocol': entry['protocol'],
                'Source IP': entry['source_ip'],
                'Source Port': entry['source_port'],
                'Destination IP': entry['destination_ip'],
                'Destination Port': entry['destination_port'],
                'Packet Size': entry['packet_size']
            })

    # Save to JSON
    with open(json_file, 'w') as f:
        json.dump(entries, f, indent=4)

    # Save threats report
    with open(threats_file, 'w') as f:
        f.write(f"THREAT REPORT - Generated : {last_timestamp}\n")
        f.write("=" * 50 + "\n")
        f.write("Suspicious IPs (3+ log appearances):\n")
        for ip, count in suspicious_ips.items():
            f.write(f"IP: {ip} | Occurrences: {count}\n")

    # Display summary
    print("=" * 60)
    print("FIREWALL LOG ANALYSIS REPORT")
    print("=" * 60)
    print(f"Total entries processed : {total_entries}")
    print(f"Valid entries parsed : {valid_entries}")
    print(f"Malformed entries skipped: {malformed}")
    print("--- Action Summary ---")
    print(f"ACCEPT : {actions.get('ACCEPT', 0)}")
    print(f"DROP : {actions.get('DROP', 0)}")
    print("--- Top 3 Targeted Destination Ports ---")
    for i, (port, count) in enumerate(top_ports, 1):
        print(f"{i}. Port {port} — {count} hits")
    print("--- Suspicious Source IPs (3+ appearances) ---")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            print(f"{ip} — {count} occurrences")
    else:
        print("None")
    print("Output saved:")
    print("output.csv")
    print("output.json")
    print("threats.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()
