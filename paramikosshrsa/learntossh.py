#!/usr/bin/env python3

## Import paramiko
import paramiko
import os

##shortcut  issueing commands remote
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr, = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

sshsession = paramiko.SSHClient()

##########
##
##

## mykey is private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

##if
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

##If
sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

##simple
our_commands=["touch sshvorked.txt", "touch create.txt", "touch files3.txt", "ls"]

##cycle
for x in our_commands:
    print(commandissue(x))


