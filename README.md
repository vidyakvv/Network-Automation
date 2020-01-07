# Network-Automation
This repo consists of python3 scripts for Network automation 


Netmiko :
Scripts uses netmiko library to connect to multiple Cisco switches and sends
set of commands in the 'commands_file.txt' to each switch

Instead of hard coding username and password, this script prompts the user
to enter username and password

The script handles exceptions while connecting instead of terminating the program

devices_ip.txt consists device ip addresses to send commands to.
