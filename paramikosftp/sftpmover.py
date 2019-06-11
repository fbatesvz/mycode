#!/usr/bin/env python3
##Moving files with SFTP

## import paramiko so we can talk with ssh
import paramiko
import os

## where to connect
t = paramiko.Transport("10.10.2.3", 22) ##  IP and Port

##HHhow to connect
t.connect(username="bender", password="alta3")

## Make a ftp 
sftp = paramiko.SFTPClient.from_transport(t)

##Make asftp connection object
sftp=paramiko.SFTPClient.from_transport(t)

##iterate
for x in os.listdir("/home/student/filestocopy/"):  #iteratw
    if not os.path.isdir("/home/stident/filestocopy/"+x):
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

sftp.close()
