import json


def read_default_settings():
    with open('../config/settings.json') as f:
        return json.load(f)


def read_default_dns_server():
    with open('../config/dns_server.json') as f:
        return json.load(f)
