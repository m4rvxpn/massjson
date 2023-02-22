import argparse
import glob
import json
import os
import subprocess
from tqdm import tqdm

def parse_masscan_output(masscan_file):
    """Parse Masscan JSON output file and return dictionary of IP addresses and their identified ports"""
    with open(masscan_file, 'r') as f:
        results = json.load(f)
    ip_ports = {}
    for result in results:
        ip = result['ip']
        if ip not in ip_ports:
            ip_ports[ip] = []
        for port in result['ports']:
            ip_ports[ip].append(port['port'])
    return ip_ports

def run_nmap_scan(ip, port, options, nmap_output_dir):
    """Run Nmap scan against an IP and port combination and write output to a file"""
    nmap_output_file = os.path.join(nmap_output_dir, f'{ip}_{port}')
    command = f'nmap {options} -oA {nmap_output_file} -p {port} {ip}'
    with open(nmap_output_file, 'w') as f:
        subprocess.run(command, shell=True, stdout=f)

def main():
    parser = argparse.ArgumentParser(description='Run Nmap scan against IP addresses and identified ports from Masscan JSON output files')
    parser.add_argument('masscan_dir', type=str, help='directory containing Masscan JSON output files')
    parser.add_argument('-o', '--output-dir', type=str, default='nmap_output', help='output directory for Nmap scan results')
    parser.add_argument('-n', '--nmap-options', type=str, default='-sV -A', help='Nmap scan options')
    args = parser.parse_args()

    masscan_files = glob.glob(os.path.join(args.masscan_dir, '*.json'))
    if not masscan_files:
        print(f'No Masscan JSON output files found in {args.masscan_dir}')
        return

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    ip_ports = {}
    for masscan_file in tqdm(masscan_files, desc='Parsing Masscan output'):
        ip_ports.update(parse_masscan_output(masscan_file))

    for ip, ports in tqdm(ip_ports.items(), desc='Running Nmap scans'):
        for port in tqdm(ports, desc=f'Scanning {ip}'):
            run_nmap_scan(ip, port, args.nmap_options, args.output_dir)

if __name__ == '__main__':
    main()
