import requests
import os
import json

def partial(username):
    if os.path.exists(f"{username}.txt"):
        print(f"[+] Saved: {username}.txt")

def check_file(username):
    if os.path.exists(f"{username}.txt"):
        print(f"[x] Removing previous file: {username}.txt")
        os.remove(f"{username}.txt")

def global_IS(username):
    print(f"Checking username {username} on global info-stealer:")
    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username={username}"
    try:
        response = requests.get(url).json()
        if len(response.get('stealers', [])) == 0:
            print("[+] No result found\n")
        else:
            for stealer in response['stealers']:
                print(f"[+] Date Compromised: {stealer['date_compromised']}")
                print(f"[+] Operating System: {stealer['operating_system']}")
                print(f"[+] Antivirus: {stealer['antiviruses']}")
                print(f"[+] Computer Name: {stealer['computer_name']}")
                print(f"[+] IP Address: {stealer['ip']}\n")
    except Exception as e:
        print(f"[!] Error checking global info-stealer: {e}")

def check_social_media(username, platform, url, not_found_text, file_handler):
    try:
        response = requests.get(url).text
        print(f"{platform}: ", end="")
        if not_found_text not in response:
            print(f"Found! {url}")
            file_handler.write(f"{url}\n")
        else:
            print("Not Found!")
    except Exception as e:
        print(f"[!] Error checking {platform}: {e}")

def scanner(username):
    print(f"Checking username {username} on social networks:")
    with open(f"{username}.txt", 'w') as file_handler:
        social_media = [
            ("Instagram", f"https://www.instagram.com/{username}", "The link you followed may be broken"),
            ("Facebook", f"https://www.facebook.com/{username}", "not found"),
            ("Twitter", f"https://www.twitter.com/{username}", "page doesn’t exist"),
            ("YouTube", f"https://www.youtube.com/{username}", "Not Found"),
            ("Blogger", f"https://{username}.blogspot.com", "HTTP/2 404"),
            ("Reddit", f"https://www.reddit.com/user/{username}", "HTTP/2 404"),
        ]

        for platform, url, not_found_text in social_media:
            check_social_media(username, platform, url, not_found_text, file_handler)

        partial(username)

def main():
    username = input("Input Username: ").strip()
    check_file(username)
    global_IS(username)
    scanner(username)

if __name__ == "__main__":
    main()
