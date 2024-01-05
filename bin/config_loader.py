import json

settings_path = '../config/settings.json'

dns_server_path = '../config/dns_server.json'


def read_default_settings():
    with open(settings_path, encoding='utf-8') as f:
        return json.load(f)


def read_default_dns_server():
    with open(dns_server_path, encoding='utf-8') as f:
        return json.load(f)


class NetConfig(object):
    interfaces = []
    dns_servers = []

    def __init__(self):
        self.interfaces = read_default_settings()['default_interfaces_name']
        set_map = read_default_dns_server()
        self.dns_servers.append(set_map['primary'])
        self.dns_servers.append(set_map['secondary'])
        for server in set_map['others']:
            self.dns_servers.append(server)


net_config = NetConfig()
