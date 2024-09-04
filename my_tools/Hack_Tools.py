import nmap
import netifaces
import ipaddress


def get_ip_range(interface='wlan0'):
    "get specific interface's ip address range"

    try:
        addresses = netifaces.ifaddresses(interface)
        ip_addr = addresses[netifaces.AF_INET][0]['addr']
        netmask = addresses[netifaces.AF_INET][0]['netmask']

        network = ipaddress.ip_network(f"{ip_addr}/{netmask}", strict=False)

        return str(network)
    
    except KeyError:
        print(f"interface {interface} don't exist or have no IPv4 address.")
        return None
    
    except Exception as e:
        print(f"can not get IP range: {e}")
        return None
    
