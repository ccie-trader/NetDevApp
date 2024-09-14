#!/user/bin/python3

import netmiko
import json
import netmiko.ssh_auth

# Basic Connection
#connection = netmiko.ConnectHandler(ip='192.168.254.241', device_type='cisco_ios', username='nde', password='automate')

# Manually accessing devices
#devices = '''
#192.168.254.241
#192.168.254.242            
#'''.strip().split()

##USING DICTIONARY TO ACCESS DEVICES

#r1 = {'ip': '192.168.254.241',
#      'device_type': 'cisco_ios',
#      'username': 'nde',
#      'password': 'automate'}
#
#r2 = {'ip': '192.168.254.242',
#      'device_type': 'cisco_ios',
#      'username': 'nde',
#      'password': 'automate'}
#
#r3 = {'ip': '192.168.254.243',
#      'device_type': 'cisco_xr',
#      'username': 'ccie',
#      'password': 'ccie'}
#	

##USING LIST OF DICTIONARIES

#devices = [
#    
#{'ip': '192.168.254.241',
#'device_type': 'cisco_ios',
#'username': 'nde',
#'password': 'automate'},
#
#{'ip': '192.168.254.242',
#'device_type': 'cisco_ios',
#'username': 'nde',
#'password': 'automate'},
#
#{'ip': '192.168.254.243',
#'device_type': 'cisco_xr',
#'username': 'ccie',
#'password': 'ccie'}
#]  

##USING A JSON FILE FOR DEVICES

with open('devices.json') as dev_file:
    devices = json.load(dev_file)

netmiko_exceptions = (netmiko.NetMikoTimeoutException,
                      netmiko.NetMikoAuthenticationException,
                      netmiko.NetmikoBaseException)

for device in devices:
    try:
        print('~'*79)
        print("Connecting to device", device['ip'])
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('show ip int brief'))

        connection.disconnect()
    except netmiko_exceptions as e:
        print("Failed to ", device['ip'], e)
    
