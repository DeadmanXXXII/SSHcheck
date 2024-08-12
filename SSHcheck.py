import paramiko
import socket

def check_ssh_user(ip, username):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip, username=username, password='invalidpassword', timeout=2)
    except paramiko.AuthenticationException:
        print(f'Username {username} is valid.')
    except paramiko.SSHException:
        print(f'Unable to establish SSH connection.')
    except socket.error:
        print(f'Connection timed out.')

if __name__ == "__main__":
    target_ip = '<target-ip>'
    with open('users.txt', 'r') as file:
        usernames = file.readlines()
        for user in usernames:
            check_ssh_user(target_ip, user.strip())
