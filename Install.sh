#!/bin/bash

# Check if Python 3.x is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3.x is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Check if Masscan is installed
if ! command -v masscan &> /dev/null
then
    echo "Masscan is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y masscan
fi

# Check if Nmap is installed
if ! command -v nmap &> /dev/null
then
    echo "Nmap is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y nmap
fi

echo "All dependencies are installed."
