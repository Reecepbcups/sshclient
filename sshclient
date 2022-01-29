#!/usr/bin/python3

# Reecepbcups | Jan 2022
# Usage: sshclient.py [server]

import sys
import subprocess

servers = {
    "craft": "craft@192.168.0.15",
    "personal": "root@ssh.website.com",
    "dig": "root@digvalidator.website.com" 
}

# output servers to user
def print_servers():
    print("\n== SERVERS ==\n", ", ".join([s for s in servers.keys()]))


def get_input():
    input_server = input("\nConnect to> ")
    connect_to_server(input_server)


def connect_to_server(server, isCLIArgument=False):
    if server in servers.keys():
        # -- is for running a command, alt is -x
        subprocess.Popen(["gnome-terminal", "--", "ssh", servers[server]])   
    else:
        print_servers()
        if not isCLIArgument:
            get_input()


def main():
    print_servers()
    get_input()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        connect_to_server(sys.argv[1], isCLIArgument=True)
    else:
        main()
