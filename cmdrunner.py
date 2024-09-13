#!/user/bin/python3

import netmiko
import json

connection = netmiko.ConnectHandler(ip='192.168.254.241', device_type='cisco_ios', username='admin', password='python')

print(connection.send_command('show ip int brief'))
