# How to Run NetSentinel

Follow the steps below to run the NetSentinel program:

1. Open the root folder named **NETSENTINEL**.
2. Navigate to the `NetSentinel` directory:
   ```bash
   cd NetSentinel
   ```
3. Start the server by running the following command:
   ```bash
   python manage.py runserver
   ```

The server should now be running, and you can access the application in your web browser.

import random

# Define a list of interface status strings with varying statuses

interface_statuses = [
'''
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0.10 192.168.1.1 YES unset administratively up down
 GigabitEthernet0/1 192.168.5.1 YES unset administratively up up
GigabitEthernet0/2 unassigned YES unset administratively down down
GigabitEthernet1/0.20 192.168.5.3 YES unset administratively up up
 GigabitEthernet1/1 192.168.5.2 YES unset administratively up up
GigabitEthernet2/2 unassigned YES unset administratively down down
Vlan1 unassigned YES unset administratively down down
''',
'''
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0.10 192.168.1.1 YES unset administratively down down
 GigabitEthernet0/1 192.168.5.1 YES unset administratively up up
GigabitEthernet0/2 unassigned YES unset administratively up down
GigabitEthernet1/0.20 192.168.5.3 YES unset administratively down up
 GigabitEthernet1/1 192.168.5.2 YES unset administratively down up
GigabitEthernet2/2 unassigned YES unset administratively down down
Vlan1 unassigned YES unset administratively up down
''',
'''
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0.10 192.168.1.1 YES unset administratively up up
 GigabitEthernet0/1 192.168.5.1 YES unset administratively down down
GigabitEthernet0/2 unassigned YES unset administratively up down
GigabitEthernet1/0.20 192.168.5.3 YES unset administratively up up
 GigabitEthernet1/1 192.168.5.2 YES unset administratively up down
GigabitEthernet2/2 unassigned YES unset administratively down down
Vlan1 unassigned YES unset administratively down up
''',
'''
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0.10 192.168.1.1 YES unset administratively down up
 GigabitEthernet0/1 192.168.5.1 YES unset administratively down down
GigabitEthernet0/2 unassigned YES unset administratively up up
GigabitEthernet1/0.20 192.168.5.3 YES unset administratively up down
 GigabitEthernet1/1 192.168.5.2 YES unset administratively down up
GigabitEthernet2/2 unassigned YES unset administratively down down
Vlan1 unassigned YES unset administratively up up
''',
'''
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0/0.10 192.168.1.1 YES unset administratively up down
 GigabitEthernet0/1 192.168.5.1 YES unset administratively up up
GigabitEthernet0/2 unassigned YES unset administratively down up
GigabitEthernet1/0.20 192.168.5.3 YES unset administratively down down
 GigabitEthernet1/1 192.168.5.2 YES unset administratively up up
GigabitEthernet2/2 unassigned YES unset administratively down down
Vlan1 unassigned YES unset administratively down up
'''
]

# Infinite loop to generate random interface output

while True: # Randomly select an interface output from the list
interface_output = random.choice(interface_statuses)

    print(interface_output)  # Print the output for demonstration
    # You can add a break condition or sleep here to avoid an infinite loop in practice
    break  # Remove this break to keep the loop running
# netsentinel
