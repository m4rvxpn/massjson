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
` python nmap_scan.py <masscan_dir> [-o <output_dir>] [-n <nmap_options>] [-t <num_threads>] `

where:

* <masscan_dir> is the directory containing Masscan JSON output files
* <output_dir> (optional) is the output directory for Nmap scan results (default is nmap_output)
* <nmap_options> (optional) are the Nmap scan options (default is -sV -A)
* <num_threads> (optional) is the number of threads to use for scanning (default is 1)

## Example
` python massjson.py /path/to/masscan/output -o /path/to/nmap/output -n "-sS -sV --version-all --script=all" `

> This will run Nmap scans against IP addresses and identified ports from Masscan JSON output files in the /path/to/masscan/output directory, using the options -sS -sV --version-all --script=all. The results will be written to the /path/to/nmap/output directory.
