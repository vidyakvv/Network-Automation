"""
This script uses netmiko library to connect to multiple Cisco switches and sends
set of commands in the 'commands_file.txt' to each switch

Instead of hard coding username and password, this script prompts the user
to enter username and password

The script handles exceptions while connecting instead of terminating the program

devices_ip.txt consists device ip addresses to send commands to.
"""
form getpass import getpass
import netmiko
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException

username = input('Enter SSH username: ')
password = getpass()

with open('commands_file.txt', 'r') as f:
    commands_to_send = f.read().splitlines()

with open('devices_ip.txt', 'r') as f:
    device_ip = f.read().splitlines()

for ip in device_ip:
    print('Connecting to device: '+ ip)
    device = {
        'device_type' = 'cisco_ios',
        'ip' = ip,
        'usernmae' = username,
        'password' = password
    }

    try :
        connection = netmiko.connectionHandler(**device)
    except(NetmikoTimeoutException):
        print('Timeout to device: '+ ip )
        continue
    except(AuthenticationException):
        print('Authentication Failure to device : '+ ip)
        continue
    except(SSHException):
        print('SSH connection issue to device : '+ ip )
        continue
    except(EOFError):
        print('End of file while attempting device : '+ ip)
        continue
    except Exception as unknown_error:
        print('Unknown Error: '+ unknown_error +' to device: ' + ip)
        continue

    print(connection)
    print(connection.send_command(commands_to_send))
    connection.disconnect()