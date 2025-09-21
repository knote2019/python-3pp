#!/usr/bin/python
import paramiko

server_ip = '192.168.122.51'
server_user = 'root'
server_passwd = 'cloud1234'
server_port = 22


def ssh_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, server_port, server_user, server_passwd)
    return ssh


def ssh_disconnect(client):
    client.close()


def exec_cmd(command):
    # 86400 seconds = 24 hours.
    stdin, stdout, stderr = ssh_connect().exec_command(command, timeout=86400)
    err = stderr.readline()

    if "" != err:
        print("command: " + command + " exec failed!\nERROR :" + err)
        return err
    else:
        print("command: " + command + " exec success.")
        return stdout


stdout = exec_cmd("docker ps")
while 1:
    line = stdout.readline()
    if line:
        print(line)
    else:
        break
