# SSHcheck.py Instructions

## Overview

This script checks SSH login credentials using the Paramiko library in Python. It attempts to connect to a specified SSH server with each combination of usernames and passwords from provided lists and reports the results.

## Requirements

1. **Python 3.x**: Ensure Python 3 is installed on your system.
2. **Paramiko Library**: This script requires the Paramiko library. Install it using pip.

## Installation

```bash
   git clone https://github.com/DeadmanXXXII/SSHcheck.git
   ```

1. **Install Dependencies**:
   Ensure you have the required libraries. You can install Paramiko, Requests and Socket using pip:

   ```bash
   pip install -f requirements.txt
   ```

2. **Prepare Your Files**:
   - **`users.txt`**: A file containing a list of usernames, one per line.
   - **`passwords.txt`**: A file containing a list of passwords, one per line.

   Ensure these files are in the same directory as the script.

## Usage

1. **Edit the Script**:
   Open the script in a text editor and replace `<target-ip>` with the IP address of the SSH server you want to test.

   ```python
   target_ip = '<target-ip>'
   ```

2. **Run the Script**:
   Execute the script from the command line:

   ```bash
   python3 sshcheck.py
   ```

   The script will attempt to connect to the specified SSH server using each username and password combination from `users.txt` and `passwords.txt`. It will print results to the console.

## Output

- **Valid Logins**: The script will print `[VALID]` if a valid username-password combination is found.
- **Invalid Logins**: The script will print `[INVALID]` if the credentials fail.
- **Errors**: Any connection or SSH-related errors will be printed with `[ERROR]`.

## Troubleshooting

1. **No Valid Logins**: If no valid logins are found but you expect some, ensure that:
   - The `users.txt` and `passwords.txt` files are correctly formatted and located in the same directory as the script.
   - The `target_ip` is correctly specified and accessible.
   - The SSH server is configured to accept connections and has valid credentials for testing.

2. **Connection Issues**: Check for network issues, server configuration, or rate limiting on the SSH server.

## Legal and Ethical Considerations

- **Permission**: Ensure you have explicit permission to test the SSH server. Unauthorized access is illegal and unethical.
- **Testing Environment**: Conduct tests in a controlled environment to avoid disruptions.

## Contact

For questions or support, please contact themadhattersplayground@gmail.com.
