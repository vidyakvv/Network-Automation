"""
This script uses netmiko library to connect to multiple Cisco switches and sends
set of commands in the 'commands_file.txt' to each switch

Instead of hard coding username and password, this script prompts the user
to enter username and password

The script handles exceptions while connecting instead of terminating the program

devices_ip.txt consists device ip addresses to send commands to based on the version (Switch or router versions)
"""
form getpass import getpass
import netmiko
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException

#Prompt for SSH username and Password
username = input('Enter SSH username: ')
password = getpass()

#Open Switch commands file
with open('commands_file_switch.txt', 'r') as f:
    commands_to_send_switch = f.read().splitlines()

#Open Router commands file
with open('commands_file_router.txt', 'r') as f:
    commands_to_send_router = f.read().splitlines()

#open ip list file
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

# Open netmiko connection and exception handling
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

    #Available versions (Switch or Router)
    list_versions = ['vios_l2-ADVENTERPRISEK9-M','VIOS-ADVENTERPRISEK9-M']

    # Check version from the device and send proper commands
    for version in list_versions:
        print('Checking software version for '+version)
        #Check device software version
        output_version = connection.send_command('show version')
        #if found run appropriate commands
        if output_version.find(version)>0 :
            print('Software version: '+ output_version)
            if version=='vios_l2-ADVENTERPRISEK9-M':
                print('Running commands for version '+ version)
                print(connection.send_command(commands_to_send_switch))
            elif version=='VIOS-ADVENTERPRISEK9-M' :
                print(connection.send_command(commands_to_send_router))
            break
        else :
            print('Not running commands for version: ' + version)
    connection.disconnect()