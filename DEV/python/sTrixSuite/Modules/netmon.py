#!/usr/bin/env python3

# - dalemueller
# - Conceived - 15/07/22
# - Network monitor

import psutil
import time

UPDATE_DELAY = 1

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

io = psutil.net_io_counters()
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

while True:
    time.sleep(UPDATE_DELAY)
    io_2 = psutil.net_io_counters()
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
    print(f"Upload: {get_size(io_2.bytes_sent)}   "
          f", Download: {get_size(io_2.bytes_recv)}   "
          f", Upload Speed: {get_size(us / UPDATE_DELAY)}/s   "
          f", Download Speed: {get_size(ds / UPDATE_DELAY)}/s      ", end="\r")
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
