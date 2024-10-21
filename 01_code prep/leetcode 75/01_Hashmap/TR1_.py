#Can you write a Python script that connects to a remote server via SSH using paramiko and retrieves a file?

import paramiko

def ssh_connect_retrieves_file(hostname,port, usr, password, remote_file_location, local_file ):
    try :
        ssh_client = paramiko.SSHClient()

        ssh_client.load_system_host_keys()

        ssh_client.connect(hostname= hostname,port= port, usr = username, password = pass)

        print("connected with remote server")
    
    except Exception as e:
        print(f"An error occured:{e}")

ssh_connect_retrieves_file = (hostname,port, usr, password, remote_file_location, local_file)

