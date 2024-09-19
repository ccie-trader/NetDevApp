#!/user/bin/python3
#GETPASS USING IMPORT COMMAND

import banner
import netmiko
import json
import netmiko.ssh_auth
import myaccess
import sys

##USING A JSON FILE FOR DEVICES

netmiko_exceptions = (netmiko.NetMikoTimeoutException,
                      netmiko.NetMikoAuthenticationException,
                      netmiko.NetmikoBaseException)

username, password = myaccess.get_credentials()

with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

print(commands) ####TESTING

with open(sys.argv[2]) as dev_file: 
    devices = dev_file.readlines()

print(devices) ####TESTING

for device in devices:
    try:
        print('~'*79)
        print("Connecting to device", device['ip'])
        connection = netmiko.ConnectHandler(**device)

        for command in commands:
            print('##Output of ' + command)
            print(connection.send_command(command))
            print()
        connection.disconnect()
    except netmiko_exceptions as e:
        print("Failed to ", device['ip'], e)

