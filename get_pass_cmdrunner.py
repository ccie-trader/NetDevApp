#!/user/bin/python3
#USING GET PASS

from getpass import getpass
import netmiko
import json
import netmiko.ssh_auth

def get_input(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)

def get_credentials():
    '''Prompts for, and returns, a username and passowrd'''

    username = get_input('Enter Username: ')
    password = None

    while not password:
        password = get_pass()
        password_verify = get_pass('Confirm password: ')
        
        if password != password_verify:
            print('Password do not match. Try again.')
            password = None
    return username, password

##USING A JSON FILE FOR DEVICES

netmiko_exceptions = (netmiko.NetMikoTimeoutException,
                      netmiko.NetMikoAuthenticationException,
                      netmiko.NetmikoBaseException)

username, password = get_credentials()

with open('devices.json') as dev_file:
    devices = json.load(dev_file)


for device in devices:
    try:
        print('~'*79)
        print("Connecting to device", device['ip'])
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('show ip int brief'))

        connection.disconnect()
    except netmiko_exceptions as e:
        print("Failed to ", device['ip'], e)
    
