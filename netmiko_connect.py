#!/user/bin/python3
from netmiko import ConnectHandler

cisco_ios = {
    'device_type': 'cisco_ios',
    'host':   '192.168.254.240',
    'username': 'admin',
    'password': 'admin'
}
connect_device = ConnectHandler(**cisco_ios)

connect_device.enable()

set_ip_address = [
    "interface ethernet0/2",
    "ip address 192.168.101.254"

    ]
config_output = connect_device.send_config_set(set_ip_address)
show_output = connect_device.send_command("show ip int brief")

print(show_output)



