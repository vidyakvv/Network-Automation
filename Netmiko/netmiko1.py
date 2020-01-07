"""
This script uses netmiko library to
connect to Cisco switch and sends
'Show ip int breif' command

Device details are stored in iosv_l2_s1 dictionary

"""

import netmiko

iosv_l2_s1 = {
    'device_type' = 'cisco_ios',
    'ip' = '192.168.122.71',
    'usernmae' = 'admin',
    'password' = 'cisco'
}

#create connection to a network device
connection = netmiko.connectionHandler(**iosv_l2_s1)
print(connection)

#print show ip interfaces
print(connection.send_command('Show ip int breif'))

#Disconnect a connection
connection.disconnect()

#will give socket error since, connection is already closed
print(connection.send_command('Show ip int breif'))