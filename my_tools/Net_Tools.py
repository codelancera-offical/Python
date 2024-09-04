import subprocess
import re
import socket

def get_ip_on_linux():
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    output = result.stdout

    match = re.search(r'wlan0:.*?inet (\d+\.\d+\.\d+\.\d+)', output, re.DOTALL)

    if match:
        return match.group(1)
    else:
        return "No IP address found for wlan0"

    
def connect_to_termux(host=None):
    private_key_path = r"C:\Users\30752\.ssh\id_rsa"
    username = "u0_a53"
    if host == None:
        host = input("please enter termux's ip: ")
    port = 8022

    # build ssh connect command
    command = [
        "ssh",
        "-i", private_key_path,
        f"{username}@{host}",
        "-p", str(port)
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"SSH connect failed: {e}")
    
def get_ip_range(interface='wlan0'):
    pass
def main():
    functions = {
        "0": get_ip_on_linux,
        "1": connect_to_termux,
    }

    print("All net operations:")
    for key, value in functions.items():
        print(f"\t{key}: {value.__name__}") # print name of function

    choice = input("Choose a net operation: ")

    if choice in functions:
        result = functions[choice]()
        if result is not None:
            print(result)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
