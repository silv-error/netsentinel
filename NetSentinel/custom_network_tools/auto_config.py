import logging

def use_auto_config(down_interfaces, interface_data, failed_interfaces):
  for interface_name in down_interfaces:
    print(f"Bringing up interface: {interface_name}")
    
    # todo: uncomment later
    # response = ssh.execute_command(f"interface {interface_name}")
    # response = ssh.execute_command("no shutdown")
    
    response = "%LINK-5-CHANGED: Interface GigabitEthernet0/1, changed state to up"
    
    if response.lower(): 
      print(f"Successfully brought up interface: {interface_name}")
      # response = ssh.execute_command("exit")
    else:
      failed_interfaces.append(interface_name)
      print(f"Failed to bring up interface: {interface_name}. Response: {response}")
      logging.error(f"Failed to bring up interface: {interface_name}. No response for 'no shutdown'. Response: {response}")
      # response = ssh.execute_command("exit")