# **BlackExec Script Documentation**

## **Introduction**

BlackExec.py is designed to facilitate the deployment of a payload onto a remote machine using the SMB (Server Message Block) protocol. It establishes an SMB connection, uploads the payload to a specified SMB share, and then schedules a task on the remote machine to execute the payload. The script provides options for local and remote connections, allowing flexibility in configuring the payload deployment process.

## **Dependencies**

The script relies on the following dependencies:

- **`smbclient`**: A Python library for interacting with SMB/CIFS shares.
- **`subprocess`**: A module for spawning new processes, used to execute shell commands.
- **`datetime`**: A module for manipulating dates and times.
- **`argparse`**: A module for parsing command-line arguments.
- **`socket`**: A module for working with network sockets.
- **`threading`**: A module for creating and managing threads.
- **`random`**: A module for generating random numbers.

Ensure that these dependencies are installed before running the script.

## **Script Functions**

The script includes several functions to facilitate the payload deployment process. The following are the main functions:

- **`netcat_thread(port)`**: Spawns a new command prompt window and starts the Netcat listener on the specified port. Used for local connections where the payload will connect back to the script's host machine.
- **`run_command(command)`**: Executes a shell command using the **`subprocess`** module.
- **`main(ip=None, username=None, password=None, local=False, remote=False)`**: Orchestrates the payload deployment process. Establishes an SMB connection, uploads the payload to the remote machine, schedules a task to execute the payload, and connects to the payload listener.

## **Usage**

The script can be executed from the command line with the following options:

```
python blackexec.py [-u USERNAME] [-p PASSWORD] [-ip IP_ADDR] [-local] [-remote REMOTE_IP]
```

The command-line arguments are as follows:

- **`u USERNAME, --username USERNAME`**: The admin username for the remote machine.
- **`p PASSWORD, --password PASSWORD`**: The admin password for the remote machine.
- **`ip IP_ADDR, --ip_addr IP_ADDR`**: The IP address of the remote machine.
- **`local, --local_ip`**: Option to create a connection to the local machine.
- **`remote REMOTE_IP, --remote_ip REMOTE_IP`**: Option to send a connection to a remote machine (default port: 2001). An optional parameter **`REMOTE_IP`** can be provided to specify the remote machine's IP address. If not specified, the default port 2001 will be used.

Ensure that the required arguments are provided when running the script.

## **Workflow**

The script follows the following workflow:

1. Establish an SMB connection using the provided username and password.
2. Upload the payload to the specified SMB share on the remote machine.
3. Schedule a task to execute the payload at a specified time.
4. Connect to the payload listener either locally or remotely.

The script handles both local and remote connections. For local connections, it spawns a Netcat listener on a random port. For remote connections, it specifies the IP address and port for the payload listener.

## **Conclusion**

The SMB payload deployment script simplifies the process of deploying a payload onto a remote machine. By leveraging the SMB protocol, it provides a secure and efficient method for uploading and executing the payload. The script's flexibility allows for different deployment scenarios, whether connecting to the local machine or sending connections to remote machines.
