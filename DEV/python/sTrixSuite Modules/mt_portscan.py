#!/usr/bin/env python3

# - Brendan McCann
# - 14/07/22
# - Multi-Threaded Port Scanner

import socket
import time
import threading
from queue import Queue
from IPy import IP

targets = input("Please enter target/s to scan: ")
port_range = 500

thread_count = 1024
print_lock = threading.Lock()
q = Queue()


def checkIP(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def getBanner(sock):
    try:
        recv = sock.recv(1024).decode().strip("\n")
        return recv
    except sock.timeout:
        return ""

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
    return

def portscan(port):
    scan_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    banner_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    banner_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    banner_sock.settimeout(0.5)
    
    try:
        con = scan_sock.connect((targets, port))
            
        with print_lock:
            try:
                banner_con = banner_sock.connect((targets, port))
                banner = getBanner(banner_sock)
                print("[*] Port " + str(port) + " is open: " + banner)
                banner_con.close()
            except TypeError:
                pass
            
            print("[*] Port " + str(port) + " is open")
        con.close()
        
    except Exception:
        pass

def main():
    for x in range(thread_count):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    start = time.time()
    for worker in range(1, port_range + 1):
        q.put(worker)
    q.join()
    end = time.time()

    print("[-] Scanned " + str(port_range) + " ports in " + str(round(end - start)) + " seconds")
    quit()


main()


# for x in range(thread_count):
#     t = threading.Thread(target=threader)
#     t.daemon = True
#     t.start()

# if "," in targets:
#     for ip in targets.split(","):
#         q.put((ip.strip(' ')))
#     q.join()
# else:
#     q.put((targets.strip(' ')))
#     q.join()

# def scan(target):
#     clean_ipaddress = checkIP(target)
#     print('\n' + "[-] Scanning Target: " + str(target))
#     start = time.time()
#     for port in range(1, port_range + 1):
#         testPort(clean_ipaddress, port)
#     end = time.time()
#     print("[-] Scanned " + str(port_range) + " ports in " + str(round(end - start)) + " seconds")
#     return