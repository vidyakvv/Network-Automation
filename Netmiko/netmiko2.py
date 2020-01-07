"""
This script uses netmiko library to connect to multiple Cisco switches and sends
set of commands in the 'commands_file.txt' to each switch

ios_devices list consists devices to send commands to.
"""

import netmiko

with open('commands_file.txt', 'r') as f:
    commands_to_send = f.read().splitlines()

iosv_l2_s1 = {
    'device_type' = 'cisco_ios',
    'ip' = '192.168.122.71',
    'usernmae' = 'admin',
    'password' = 'cisco'
}
iosv_l2_s2 = {
    'device_type' = 'cisco_ios',
    'ip' = '192.168.122.72',
    'usernmae' = 'admin',
    'password' = 'cisco'
}

ios_devices = [iosv_l2_s1, iosv_l2_s2]

for device in ios_devices:
    connection = netmiko.connectionHandler(**device)
    print(connection)
    print(connection.send_command(commands_to_send))
    connection.disconnect()
