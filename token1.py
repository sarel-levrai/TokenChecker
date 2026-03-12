import requests
import time
from pystyle import System, Center, Colors, Colorate

def check_token(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = {"Authorization": token}

    try:
        r =requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            print(Colors.green + f"[+] {token}")
            return "valid"

        elif r.status_code == 401:
            print(Colors.red + f"[-] {token}")
            return "invalid"

        else:
            print(f"[ERROR {r.status_code}] {token}")
            return "invalid"

    except requests.exceptions.RequestException:
        print(f"[REQUEST ERROR] {token}")
        return "invalid"

def main():
    System.Title("TokenChecker ^| made by sarel_levrai. ^| discord.gg/nsm")
    print(Center.XCenter(Colorate.Horizontal(Colors.purple_to_blue , """ ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █  ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
             ░ ░  ░  ░      ░  ░         ░ ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                           ░                       ░                               """, 1)))
    try:
        with open("tokens.txt", "r", encoding="utf-8") as f:
            tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("tokens.txt not found")
        return

    valid = []
    invalid = []

    for token in tokens:
        result = check_token(token)

        if result == "valid":
            valid.append(token)
        else:
            invalid.append(token)

        time.sleep(1)

    with open("valid.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(valid))

    with open("invalid.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(invalid))

    print(Colors.white + "\nCheck finished")
    print(Colors.white + f"Valid tokens: {len(valid)}")
    print(Colors.white + f"Invalid tokens: {len(invalid)}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()