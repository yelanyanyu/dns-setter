import subprocess
import re
import psutil
import sys
import config_loader


# def get_connected_interfaces():
#     # Run the command to get all network interfaces
#     command = 'netsh interface show interface'
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
#     # Find all connected interfaces
#     connected_interfaces = re.findall(r'已连接\s+专用\s+(以太网|WLAN)[^\r\n]*', result.stdout)
#     return [iface.split()[-1] for iface in connected_interfaces]


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
    interfaces = config_loader.net_config.interfaces

    # Set DNS for the single connected interface
    dns_servers = config_loader.net_config.dns_servers
    set_dns(interfaces[0], dns_servers)
