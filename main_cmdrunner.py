#!/user/bin/python3
#GETPASS USING IMPORT COMMAND

import netmiko.exceptions
import banner
import netmiko
import json
import netmiko.ssh_auth
import myaccess
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C

if len(sys.argv) < 3:
    print("Usage: access_cmdrunner.py commands.txt devices.json")
    exit()

##USING A JSON FILE FOR DEVICES

netmiko_exceptions = (netmiko.exceptions.NetMikoTimeoutException,
                      netmiko.exceptions.NetMikoAuthenticationException,
                     )
                      

username, password = myaccess.get_credentials()

with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

with open(sys.argv[2]) as dev_file: 
    ios_devices = json.load(dev_file)

for device in ios_devices:
    device['username'] = username
    device['password'] = password
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

