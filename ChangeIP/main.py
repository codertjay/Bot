import os

def change_ip(interface_name, new_ip, subnet_mask):
    # As an administrator, assign a new IP address to the interface
    cmd = f"sudo ifconfig {interface_name} {new_ip} netmask {subnet_mask}"
    os.system(cmd)

# Usage
new_ip = "192.168.1.100"
subnet_mask = "255.255.255.0"
interface_name = "wlp2s0"  # Change this to the specific network interface you want to modify

change_ip(interface_name, new_ip, subnet_mask)
