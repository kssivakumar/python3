#!/usr/bin/env python3.6
# Script to donwload from the remote server using sftp.
import paramiko
import pysftp
rhostname = "plkopsat001"
rusername = "siva.a.saravanamuthu"
rpassword = "/home/siva.a.saravanamuthu/.ssh/id_rsa"


with pysftp.Connection(host=rhostname, username=rusername, private_key=rpassword) as sftp:
    print('Connection is successful')
    remotepath = '/home/siva.a.saravanamuthu/patch/'
    localpath = '/home/siva.a.saravanamuthu/sftptest/'
    # Change it to put to upload directories.
    sftp.get_d(remotepath, localpath, preserve_mtime=False)
    print('Download Completed')
