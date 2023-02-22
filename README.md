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
To use the tool, navigate to the directory containing the masscan_to_nmap.py script and run the following command:

` python massjson.py json_folder `

where json_folder is the path to the folder containing the Masscan JSON output files.

The tool will map the IP addresses to their open ports using the Masscan JSON files and then run Nmap scans on each IP address and port combination. The Nmap scan results will be saved in a separate .txt file for each IP address.

## Example
Suppose you have a folder named masscan_output containing Masscan JSON output files. To run Nmap scans on the IP addresses and ports identified by Masscan, navigate to the masscan-to-nmap-tool directory and run the following command:

` python massjson.py masscan_output `

>The tool will map the IP addresses to their open ports using the Masscan JSON files in the masscan_output folder and then run Nmap scans on each IP address and port combination. The Nmap scan results will be saved in separate .txt files for each IP address in the same directory.
