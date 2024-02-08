import time
from datetime import datetime as dt
import os

# Site names to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

# hosts file paths for different operating systems
Linux_hosts_file = "/etc/hosts"
Windows_hosts_file = r"C:\Windows\System32\drivers\etc\hosts"

# default hosts file based on the current operating system
default_hosts_file = Linux_hosts_file if os.name == 'posix' else Windows_hosts_file

# IP address to which the blocked sitel will be redirected
redirect_ip = "127.0.0.1"

def block_websites(start_hour, end_hour):
    """
    Blocking specified websites during certain hours.
    """
    while True:
        try:
            current_time = dt.now()
            if (dt(current_time.year, current_time.month, current_time.day, start_hour) < current_time <
                dt(current_time.year, current_time.month, current_time.day, end_hour)):
                print("Focus mode: Blocking websites...")
            else:
                print("Free time: Websites unblocked.")
            time.sleep(3)
        except PermissionError as e:
            print(f"Permission error: {e}. Try running the script as an administrator.")
            break