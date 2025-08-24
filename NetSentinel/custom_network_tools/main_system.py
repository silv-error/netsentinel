import requests
import random
import time
import asyncio
import json

from constants.interface_status import INTERFACE_BRIEF_DATA
from services.deepseek import query_deepseek
from services.ssh import *
from auto_config import use_auto_config

async def main():
    # TODO: uncomment
    # * THIS IS FOR CONNECTING TO CISCO DEVICE, UNCOMMONT THIS FOR TESTING WITH REAL DEVICE
    # ssh = SSH(ip="192.168.1.254", username="admin", password="cisco", enable_password="cisco")
    # ssh.connect()
    
    # down_interface_ips = []
    # still_down_interfaces = []
    failed_interfaces = []
    
    while True:
        # ssh.execute_command("do show ip interface brief")
        # down_interfaces.clear()
        
        # SOME RANDOM NETWORK STATUS
        interface_output = random.choice(INTERFACE_BRIEF_DATA)
        
        # FILTER ALL DOWN INTERFACES USING DEEPSEEK AI
        down_interfaces = await query_deepseek(
            query='Can you get all the interface with assigned IP Address and down in protocol? If none please dont respond',
            cisco_output=interface_output,
            answer_format='''
                Answer format:
                interface name
            '''
        )
        
        # FILTER ALL UP INTERFACES USING DEEPSEEK AI
        up_interfaces = await query_deepseek(
            query='Can you get all the interface with assigned IP address and up in protocol? If none please dont respond',
            cisco_output=interface_output,
            answer_format='''
                Answer format:
                interface name
            '''
        )
        
        # GET IP ADDRESSES WITH UP INTERFACES
        up_ip = await query_deepseek(
            query='Can you get all the IP Address that is up protocol? If none pleasee dont respond',
            cisco_output=interface_output,
            answer_format='''
                Answer format:
                ip address
            '''
        )
        
        # GET IP ADDRESSES WITH DOWN INTERFACES
        down_ip = await query_deepseek(
            query='Can you get all the IP Address that is down protocol? If none please dont respond',
            cisco_output=interface_output,
            answer_format='''
                Answer format:
                ip address
            '''
        )
        
        interface_data = [] # Create a list to hold all formated interface data

        # Process the up interfaces
        for interface_name, ip in zip(up_interfaces, up_ip):
            export_data = {
                "interface": interface_name,
                "status": "Online",
                "ip": ip,
                "protocol": "up"
            }
            interface_data.append(export_data)

        # Process the down interfaces
        for interface_name, ip in zip(down_interfaces, down_ip):
            export_data = {
                "interface": interface_name,
                "status": "Offline",
                "ip": ip,
                "protocol": "down"
            }
            interface_data.append(export_data)

        # Send all interface data in a single POST request
        url = "http://127.0.0.1:8000/api/send_status"
        requests.post(url, json=interface_data)
        
        print("interfaces data", json.dumps(interface_data))

        if down_interfaces == ["none"]:
            print("No interfaces are down with an IP address. Checking again...")
            time.sleep(10)
            continue
        
        # TROUBLESHOOT FUNCTION
        use_auto_config(down_interfaces, interface_data, failed_interfaces)
                
        print("Checking again...")
        print("==================================================")
        time.sleep(10)
        continue

        # Check the status of interfaces again
        # interface_output_after = ssh.check_interfaces()
        
        # still_down_interfaces.clear()
        # still_down_interfaces = query_deepseek(interface_output_after)

        # if still_down_interfaces != ["none"]:
        #     for interface_name in still_down_interfaces:
        #         # Get the IP address of the down interface
        #         command = f"do show run | include {interface_name}"
        #         config_output = ssh.execute_command(command)
        #         down_interface_ips.append(config_output.strip())
        #         logging.info(f"Interface {interface_name} is still down. Configuration: {config_output}")

        #     # Query AI for network address determination
        #     network_addresses = []
        #     for ip_config in down_interface_ips:
        #         response = query_deepseek(ip_config)
        #         network_addresses.append(response)

        #     # Log the determined network addresses
        #     for network in network_addresses:
        #         logging.info(f"Determined network address: {network}")

        break 

    # todo: uncomment
    # ssh.close()

if __name__ == "__main__":
    asyncio.run(main())
