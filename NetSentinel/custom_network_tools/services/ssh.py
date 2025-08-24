import paramiko
import time

def read_channel_output(channel, timeout=2):
    output = ""
    end_time = time.time() + timeout
    while True:
        if channel.recv_ready():
            received = channel.recv(1024).decode('utf-8')
            output += received
            end_time = time.time() + timeout
        if time.time() > end_time:
            break
        time.sleep(0.2)
    return output

class SSH:
    def __init__(self, ip, username, password, enable_password):
        self.ip = ip
        self.username = username
        self.password = password
        self.enable_password = enable_password
        self.client = None
        self.channel = None

    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.ip, username=self.username, password=self.password)
            print(f"Successfully connected to {self.ip}")
            self.channel = self.client.invoke_shell()
            time.sleep(1)  # Delay to let the shell be ready
            self.channel.send("enable\n")
            time.sleep(0.5)
            self.channel.send(f"{self.enable_password}\n")
            time.sleep(0.5)
            print("Entered enable mode.")
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def execute_command(self, command):
        """Execute a command on the device and return the output."""
        self.channel.send(command + "\n")
        time.sleep(0.5)
        return read_channel_output(self.channel, timeout=2)

    def close(self):
        if self.client:
            self.client.close()