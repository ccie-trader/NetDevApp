import netmiko
import json

connect = netmiko.ConnectHandler(ip = '192.168.254.243', 
                                 device_type = 'cisco_xr', 
                                 username = 'ccie', 
                                 password = 'ccie')

print(connect.send_command("show ip interface brief"))

