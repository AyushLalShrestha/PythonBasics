# Running paramiko commands

import paramiko 

ssh = paramiko.SSHClient()
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

# If you're using SSH keys, first prepare the keyfile (id_rsa private key file) using EITHER: 
k = paramiko.RSAKey.from_private_key_file(keyfilename) 

# or
# k = paramiko.DSSKey.from_private_key_file(keyfilename)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host, username=user, pkey=k)