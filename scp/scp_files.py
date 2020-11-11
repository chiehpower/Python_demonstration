import paramiko
from scp import SCPClient
import sys

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


# ssh = SSHClient()
# ssh.load_system_host_keys()
# ssh.connect('example.com')

your_ip = ''
port = 22
account_name = ''
passward = ''

ssh = createSSHClient(your_ip, port, account_name, passward)


def progress4(filename, size, sent, peername):
    sys.stdout.write("(%s:%s) %s's progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
    

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport(), progress4=progress4)

# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
scp.put('test', recursive=True, remote_path='/home/user/')

scp.close()

