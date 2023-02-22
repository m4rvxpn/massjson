import json
import subprocess
import os
import argparse

def map_ips_to_ports(json_folder):
    # Create an empty dictionary for storing IP addresses and their associated ports
    ip_port_dict = {}

    # Loop through each file in the folder
    for filename in os.listdir(json_folder):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Open and read the JSON file
            with open(os.path.join(json_folder, filename), 'r') as json_file:
                json_data = json.load(json_file)

            # Create a dictionary of IP addresses and their open ports from the JSON data
            for entry in json_data:
                ip_address = entry['ip']
                port_list = [int(port.split('/')[0]) for port in entry['ports'].split(',')]
                if int(ip_address.replace('.', '')) in ip_port_dict:
                    # If the IP address already exists in the dictionary, merge the new port list with the existing one
                    ip_port_dict[int(ip_address.replace('.', ''))] = list(set(ip_port_dict[int(ip_address.replace('.', ''))] + port_list))
                else:
                    # If the IP address does not yet exist in the dictionary, add it with its port list
                    ip_port_dict[int(ip_address.replace('.', ''))] = port_list

    return ip_port_dict

def run_nmap_scan(ip_port_dict):
    # Run Nmap scans on each IP address and port combination in the dictionary
    for ip_address, port_list in ip_port_dict.items():
        ip_address_str = f"{ip_address//1000000}.{(ip_address//1000)%1000}.{ip_address%1000}"
        port_str = ','.join([str(port) for port in port_list])
        print(f"Running Nmap scan on {ip_address_str} with ports {port_str}...")
        command = f"nmap -sC -sV -p {port_str} -oN {ip_address_str}.txt {ip_address_str}"
        subprocess.call(command, shell=True)

if __name__ == "__main__":
    # Set up command line arguments for the JSON folder path
    parser = argparse.ArgumentParser()
    parser.add_argument('json_folder', help='Path to folder containing Masscan JSON output files')

    # Parse the command line arguments
    args = parser.parse_args()

    # Use the command line argument to map IPs to ports and run Nmap scans
    ip_port_dict = map_ips_to_ports(args.json_folder)
    run_nmap_scan(ip_port_dict)
