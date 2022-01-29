# sshclient
Application to make scaling ssh connections easier for many machines **LINUX ONLY**

# Setup
- Clone Repo / Copy code to a python file
- Set up server names & ssh URI's *(user@192.168.0.1)* within dictionary {}
- update terminal emulator *(gnome-terminal by default for ubuntu)*
- Ensure all servers have your public key *ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}*
- chmod +x sshclient.py
- ./sshclient.py [server]

*Place the file within a folder found in $PATH to call the file as just `sshclient [server]` from terminal*

# Usage
./sshclient.py myserver
