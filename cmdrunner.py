#!/user/bin/python3

import netmiko
import json

import netmiko.ssh_auth

# Basic Connection
connection = netmiko.ConnectHandler(ip='192.168.254.241', device_type='cisco_ios', username='nde', password='automate')

print(connection.send_command('show ip int brief'))



