import subprocess
import re
import psutil
import sys


class Net(object):
    def __init__(self, net_name, description, mac_address,
                 is_dhcp, is_autoconfig, ipv6_address, subnet_mask,
                 gateway, dhcp_server, dns_server, net_bios):
        self.net_name = net_name
        self.description = description
        self.mac_address = mac_address
        self.is_dhcp = is_dhcp
        self.is_autoconfig = is_autoconfig
        self.ipv6_address = ipv6_address
        self.subnet_mask = subnet_mask
        self.gateway = gateway
        self.dhcp_server = dhcp_server
        self.dns_server = dns_server
        self.net_bios = net_bios

    def __str__(self):
        return f"Network Name: {self.net_name}\n" \
               f"Description: {self.description}\n" \
               f"MAC Address: {self.mac_address}\n" \
               f"DHCP Enabled: {self.is_dhcp}\n" \
               f"Autoconfiguration Enabled: {self.is_autoconfig}\n" \
               f"IPv6 Address: {self.ipv6_address}\n" \
               f"Subnet Mask: {self.subnet_mask}\n" \
               f"Default Gateway: {self.gateway}\n" \
               f"DHCP Server: {self.dhcp_server}\n" \
               f"DNS Server: {self.dns_server}\n" \
               f"NetBIOS over Tcpip Enabled: {self.net_bios}\n"


def get_connected_interfaces():
    # Run the command to get all network interfaces
    command = 'netsh interface show interface'
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    # Find all connected interfaces
    connected_interfaces = re.findall(r'已连接\s+专用\s+(以太网|WLAN)[^\r\n]*', result.stdout)
    return [iface.split()[-1] for iface in connected_interfaces]


def get_all_interfaces_name():
    return psutil.net_if_stats().keys()


def set_dns(interface_name, dns_servers):
    """
    Run shell code for dns update.
    :param interface_name: .
    :param dns_servers: .
    :return: .
    """
    # Set the primary DNS server
    subprocess.run(f'netsh interface ipv4 set dnsservers name="{interface_name}" static {dns_servers[0]} primary',
                   shell=True)

    # Set the secondary and tertiary DNS servers
    for index, dns in enumerate(dns_servers[1:], start=2):
        subprocess.run(f'netsh interface ipv4 add dnsservers name="{interface_name}" address={dns} index={index}',
                       shell=True)

    print(f"DNS servers have been updated for {interface_name}")


def do_set_dns():
    """
    Truly set the dns server for current user.
    """
    # Get the list of connected interfaces
    interfaces = get_connected_interfaces()

    # Check the number of connected interfaces
    if len(interfaces) > 1 or len(interfaces) < 0:
        print("Error: The number of connected networks should be zero or one.")
        sys.exit(1)
    elif len(interfaces) == 0:
        print("No connected network found. Exiting program.")
        sys.exit(0)
    else:
        # Set DNS for the single connected interface
        dns_servers = ["223.5.5.5", "10.1.1.9", "223.6.6.6"]
        set_dns(interfaces[0], dns_servers)
