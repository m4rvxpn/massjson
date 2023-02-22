# MassJson

This Python tool can be used to automate the process of running Nmap scans on IP addresses and ports identified by Masscan scans. It takes a folder containing Masscan JSON output files as input, maps the IP addresses to their open ports, and then runs Nmap scans on each IP address and port combination.

## Requirements
* Python 3.x
* Masscan
* Nmap

## Installation
Install Masscan and Nmap on your system.
Clone or download the massjson repository to your local machine.
To install the necessary dependencies using the provided bash script, follow these steps:

* Download the bash script from the GitHub repository.

* Open a terminal window and navigate to the directory where you downloaded the script.

* Run the following command to make the script executable:

`chmod +x install_dependencies.sh`

* Run the script with superuser privileges using the following command:

` sudo ./install_dependencies.sh `
* The script will prompt you for your password. Enter it and press Enter.

* The script will then install Python 3.x, Masscan, and Nmap on your system.

* Once the installation is complete, you can verify that the dependencies were installed correctly by running the following commands:

` python3 --version `
` masscan --version `
` nmap --version `

These commands should output the respective versions of Python, Masscan, and Nmap that were installed by the script.

## Usage
` python masscan_nmap_scanner.py <masscan_dir> [-o <output_dir>] [-n <nmap_options>] `
* masscan_dir: The directory containing Masscan JSON output files. Required.
* -o <output_dir> or --output-dir <output_dir>: The output directory for Nmap scan results. Default is nmap_output.
* -n <nmap_options> or --nmap-options <nmap_options>: The Nmap scan options to use. Default is -sV -A.

## Example
` python masscan_nmap_scanner.py /path/to/masscan/output -o /path/to/nmap/output -n "-sS -sV --version-all --script=all" `

> This will run Nmap scans against IP addresses and identified ports from Masscan JSON output files in the /path/to/masscan/output directory, using the options -sS -sV --version-all --script=all. The results will be written to the /path/to/nmap/output directory.
