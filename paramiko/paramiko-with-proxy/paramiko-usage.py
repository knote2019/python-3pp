#!/usr/bin/python
import os
import paramiko

server_ip = '192.168.99.100'
server_user = 'docker'
server_passwd = 'tcuser'
server_port = 22


def secure_copy(user, host, src, dest, key_filename=None, allow_agent=True):
    keys = _load_keys(key_filename, allow_agent)
    pkey = keys[0]
    ssh = paramiko.SSHClient()
    proxy = None
    ssh_config_file = os.path.expanduser("~/.ssh/config")
    if os.path.exists(ssh_config_file):
        conf = paramiko.SSHConfig()
        with open(ssh_config_file) as f:
            conf.parse(f)
        host_config = conf.lookup(host)
        if 'proxycommand' in host_config:
            proxy = paramiko.ProxyCommand(host_config['proxycommand'])
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, pkey=pkey, sock=proxy)
    scp = SCPClient(ssh.get_transport())
    scp.get(src, dest)
    scp.close()
