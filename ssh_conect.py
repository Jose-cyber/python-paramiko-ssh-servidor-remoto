import paramiko
from paramiko.client import AutoAddPolicy

# informações necessarias para a conexão com o servidor 
address = "127.0.0.1" 
username = "usuario"
password = "cucabeludo"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=address, username=username, password=password)

#defina dentro dos parentes no exec_command o comando que você quer executar
stdin, stdout, stderr = ssh.exec_command('touch olaparamiko')
ssh.close()


