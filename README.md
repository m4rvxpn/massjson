# MassJson

This Python tool can be used to automate the process of running Nmap scans on IP addresses and ports identified by Masscan scans. It takes a folder containing Masscan JSON output files as input, maps the IP addresses to their open ports, and then runs Nmap scans on each IP address and port combination.

## Requirements
* Python 3.x
* Masscan
* Nmap

## Installation
Install Masscan and Nmap on your system.
Clone or download the masscan-to-nmap-tool repository to your local machine.
Install the required Python libraries by running pip install -r requirements.txt.

## Usage
To use the tool, navigate to the directory containing the masscan_to_nmap.py script and run the following command:

` python massjson.py json_folder `

where json_folder is the path to the folder containing the Masscan JSON output files.

The tool will map the IP addresses to their open ports using the Masscan JSON files and then run Nmap scans on each IP address and port combination. The Nmap scan results will be saved in a separate .txt file for each IP address.

## Example
Suppose you have a folder named masscan_output containing Masscan JSON output files. To run Nmap scans on the IP addresses and ports identified by Masscan, navigate to the masscan-to-nmap-tool directory and run the following command:

` python massjson.py masscan_output `

>The tool will map the IP addresses to their open ports using the Masscan JSON files in the masscan_output folder and then run Nmap scans on each IP address and port combination. The Nmap scan results will be saved in separate .txt files for each IP address in the same directory.
