#!/usr/bin/python3

# Reecepbcups | Jan 2022
# Usage: sshclient.py [server] [view]
# Other: sshclient.py all view (shows all ips & storage used)


import sys
import os
import subprocess as sp

servers = {
    "craft": "craft@192.168.0.15",
    "personal": "root@ssh.website.com",
    "dig": "root@digvalidator.website.com",
}

# output servers to user
def print_servers():
    print("\n== SERVERS ==\n")
    print(", ".join([s for s in servers.keys()]))


def get_input():
    input_server = input("\nConnect to> ")
    connect_to_server(input_server)

def checkStorage(server):
    # custom ports dont work yet
    # x = sp.check_output(["ssh", f"{servers[server]}", "-q" ,"-t", "df -h /", "2> /dev/null"]).decode('utf-8')
    x = sp.check_output(f"ssh {servers[server]}".split(" ") + ["-q", "-t", "df -h /", "2> /dev/null"]).decode('utf-8')
    # print(x); sys.exit()
    for line in x.split("\n"):
        if '%' in line and "/" in line:
            return line
    return ""

def connect_to_server(server, isCLIArgument=False):
    if server not in servers.keys():    
        print_servers()
        if not isCLIArgument:
            get_input()

    os.system(f"ssh {servers[server]}") # gnome-terminal -- ssh <server>


def main():
    print_servers()
    get_input()

# add way to ssh-copy-id SERVER

def output_server_info(server):
    print("\n\t" + server, "\n-> ", servers[server])
    print("-> ", checkStorage(server))
    print()

if __name__ == "__main__":
    argCount = len(sys.argv)

    if argCount > 1:
        serverName = sys.argv[1]

        if argCount == 3: # sshclient server v
            if sys.argv[2].lower() in ['v', 'view']:
                if serverName == 'all':
                    for server in servers:
                        output_server_info(server)
                else:
                    output_server_info(serverName)
                sys.exit()

        connect_to_server(serverName, isCLIArgument=True)

    else:
        main()