import paramiko

test_host = "xx.xx.xx.xx"
access_user = "user"
key = paramiko.RSAKey.from_private_key_file("/Users/key-dir/key.pem")

with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=test_host, username=access_user, pkey=key)
    stdin, stdout, stderr = ssh.exec_command('ls')
    for line in stdout:
        print('...' + line.strip('¥n'))