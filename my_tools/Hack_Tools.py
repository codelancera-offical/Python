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


def scan_network(ip_range):

    nm = nmap.PortScanner()
    try:
        print(f"Scanning IP range: {ip_range}")
        nm.scan(hosts=ip_range, arguments='-sn')  # 使用 -sn 执行主机发现（ping 扫描）
        for host in nm.all_hosts():
            print(f"host: {host}, status: {nm[host].state()}")
    except Exception as e:
        print(f"error in scanning: {e}")
