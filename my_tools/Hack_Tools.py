import nmap
import netifaces
import ipaddress
import platform
import subprocess

# Net-Hack
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
        nm.scan(hosts=ip_range, arguments='-sn -PE -PS80,443 -PA22,25,80')  # 使用 -sn 执行主机发现（ping 扫描）
        for host in nm.all_hosts():
            print(f"host: {host}, status: {nm[host].state()}")
    except Exception as e:
        print(f"error in scanning: {e}")


import os
import platform
import subprocess

def ping_ip(ip):
    """Ping 一个 IP 地址"""
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def scan_network_via_ping(ip_range):
    """Ping 扫描整个 IP 范围"""
    ip_base = ".".join(ip_range.split('.')[:-1])
    active_ips = []

    for i in range(1, 255):  # 扫描 1 到 254 号主机
        ip = f"{ip_base}.{i}"
        if ping_ip(ip):
            active_ips.append(ip)
            print(f"主机 {ip} 是开机状态")
        else:
            print(f"主机 {ip} 无响应")

    return active_ips


# Encode-Hack
import base64

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        raise