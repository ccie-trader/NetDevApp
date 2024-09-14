#!/user/bin/python3

import netmiko
import json

import netmiko.ssh_auth

# Basic Connection
#connection = netmiko.ConnectHandler(ip='192.168.254.241', device_type='cisco_ios', username='nde', password='automate')

# Using a for loop
devices = '''
192.168.254.241
192.168.254.242            
'''.strip().split()

for device in devices:
    try:
        print('~'*79)
        print("Connecting to device", device)
        connection = netmiko.ConnectHandler(ip = device,
                                            device_type = "cisco_ios",
                                            username = "nde",
                                            password = "automate")


        print(connection.send_command('show ip int brief'))

        connection.disconnect()
    except netmiko.ssh_auth.NetMikoAuthenticationException:
        print("Authentication Error")


