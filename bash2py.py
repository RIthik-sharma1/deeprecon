import requests
import json
import os

# Define banner
def banner():
    print('''\033[1;77m
      __  _  __      _  _      _  __   _  ____ 
|  | |                   _ |    |            |  |       | |       ||    _ |
|  | |    __    _   |     |    _      |_|   _        _   | 
|  |_|   |__ |   |_ |   |__   |   |_ |           | |      |_ |   |__ 
|       __      _      |  |    _     _     |_|       _      |
|       | __|    |_ |   |  | |  |   |    |    | |             |___ |   |  | |
|_____|  |_|  |_|    |__|  |__| |__|  |_|
    \033[0m''')
    print("\033[1;93m             .:.:;..\033[0m\033[1;77m UserFinder v1.0 Developer: misha korzhik \033[0m\033[1;93m..;:.:.\033[0m\n")

# Remove previous file if exists
def check_file(username):
    if os.path.exists(f"{username}.txt"):
        print(f"\033[1;92m[\033[0m\033[1;77mx\033[0m\033[1;92m] Removing previous file: \033[0m\033[1;77m {username}.txt")
        os.remove(f"{username}.txt")
        print("\n\n")
    else:
        print("\n")

# Check username on global info-stealer
def global_IS(username):
    print(f"\033[1;92m[\033[0m\033[1;77m>\033[0m\033[1;92m] Checking username \033[0m\033[1;77m {username} \033[0m\033[1;92m on global info-stealer: \033[0m")
    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username={username}"
    response = requests.get(url).json()
    
    if len(response.get('stealers', [])) == 0:
        print("\033[1;77m[\033[0m\033[1;92m+\033[0m\033[1;77m] No result found\n\n")
    else:
        for stealer in response['stealers']:
            date_compromised = stealer.get('date_compromised', 'N/A')
            operating_system = stealer.get('operating_system', 'N/A')
            computer_name = stealer.get('computer_name', 'N/A')
            antiviruses = stealer.get('antiviruses', 'N/A')
            ip = stealer.get('ip', 'N/A')

            print(f"\033[1;77m[\033[0m\033[1;92m+\033[0m\033[1;77m] Date compromised: {date_compromised}")
            print(f"\033[1;77m[\033[0m\033[1;92m+\033[0m\033[1;77m] Operating system: {operating_system}")
            print(f"\033[1;77m[\033[0m\033[1;92m+\033[0m\033[1;77m] Computer name   : {computer_name}")
            print(f"\033[1;77m[\033[0m\033[1;92m+\033[0m\033[1;77m] IP address      : {ip}\n")

# Check social networks
def check_social_network(username, network, url_template, success_msg, fail_msg):
    url = url_template.format(username)
    response = requests.get(url, headers={"Accept-Language": "en"})
    
    if response.status_code == 200:
        print(f"\033[1;92m Found! \033[0m {url}")
        with open(f"{username}.txt", "a") as f:
            f.write(f"{url}\n")
    else:
        print(f"\033[1;93m{fail_msg}\033[0m")

def scanner(username):
    print(f"\033[1;92m[\033[0m\033[1;77m>\033[0m\033[1;92m] Checking username \033[0m\033[1;77m {username} \033[0m\033[1;92m on social networks: \033[0m")

    # Check on Instagram
    check_social_network(username, "Instagram", "https://www.instagram.com/{}", "Found!", "Not Found!")

    # Check on Facebook
    check_social_network(username, "Facebook", "https://www.facebook.com/{}", "Found!", "Not Found!")

    # More social networks can be added similarly...

# Main
if name == "main":
    banner()
    username = input("\033[1;92m[\033[0m\033[1;77m>\033[0m\033[1;92m] Input Username:\033[0m ")
    check_file(username)
    global_IS(username)
    scanner(username)
