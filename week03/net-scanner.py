import subprocess
import fire
import socket
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from ipaddress import ip_address

open_ports = []


def ping_ip(ip_address):
    # Ping one IP and print its address
    try:
        res = subprocess.run(["ping", ip_address, "-t", "2"], capture_output=True)
        if res.returncode == 0:
            print(ip_address)
    except Exception as e:
        print(e)


def tcp_test(ip_port_tuple):
    # Use socket to connect IP and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        return_code = s.connect_ex(ip_port_tuple)
    except OSError as e:
        print('OS Error:', e)

    if return_code == 0:
        print("Connected.")
        open_ports.append(ip_port_tuple[1])
    else:
        print('Unable to connect.')


def ping_func(n, f, ip):
    #
    if f == 'ping':
        if '-' in ip:
            start_ip, stop_ip = ip.split('-')
            start_last_num = start_ip.split('.')[-1]
            stop_last_num = stop_ip.split('.')[-1]
            start_head = start_ip.rstrip(start_last_num).rstrip('.')
            seed = [start_head + '.' + str(num) for num in range(int(start_last_num), int(stop_last_num) + 1)]
            with ThreadPoolExecutor(n) as executor:
                executor.map(ping_ip, seed)
        else:
            ping_ip(ip)
    elif f == 'tcp':
        seed = [(ip, port) for port in range(0, 65536)]
        with ThreadPoolExecutor(n) as executor:
            executor.map(tcp_test, seed)
        print(f'On {ip}, open port is ：{open_ports}\n')
    else:
        print("You can only test IP or opened ports ")

fire.Fire(ping_func)
