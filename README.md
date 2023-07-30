The program performs an ARP scan on the local network to discover devices (hosts) connected to it. 
The script utilizes the scapy library to send ARP packets and receive responses from devices in the network. 
It then displays the IP addresses, MAC addresses, and hostnames (if available) of the discovered devices.

To install the program, enter the command:
pip install -r requirements.txt

After running this program, an ARP scan will be conducted on the local network (default subnet is 192.168.0.0/24), 
and the discovered devices will be shown with their IP addresses, MAC addresses, and hostnames (if available).

Scanning devices without the consent of other users violates their rights and may be illegal.

The program was created by keno.