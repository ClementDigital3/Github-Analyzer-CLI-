import requests
from colorama import Fore, Style, init
init(autoreset=True)

from app.utils import safe


while True:
    print("\n" + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "GITHUB ANALYZER TOOL")
    print("=" * 40 + "\n")

    username = input(Fore.WHITE + "Enter GitHub username (or type 'exit'): ").strip()

    if username.lower() == "exit":
        print(Fore.RED + "\nExiting tool. Goodbye.")
        break

    if not username:
        print(Fore.RED + "\nNo username entered.")
        continue

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n" + "=" * 40)
        print(Fore.CYAN + Style.BRIGHT + "USER REPORT")
        print("=" * 40 + "\n")

        print(Fore.GREEN + "Name: " + Fore.WHITE + str(safe(data.get("name"))))
        print(Fore.YELLOW + "Bio: " + Fore.WHITE + str(safe(data.get("bio"))))
        print(Fore.MAGENTA + "Company: " + Fore.WHITE + str(safe(data.get("company"))))
        print(Fore.BLUE + "Public Repos: " + Fore.WHITE + str(data.get("public_repos", 0)))
        print(Fore.CYAN + "Followers: " + Fore.WHITE + str(data.get("followers", 0)))
        print(Fore.WHITE + "Following: " + Fore.GREEN + str(data.get("following", 0)))
        print(Fore.GREEN + "Profile: " + Fore.BLUE + str(data.get("html_url")))

        score = data.get("public_repos", 0) + data.get("followers", 0)
        print(Fore.RED + "\nDeveloper Score: " + Fore.YELLOW + str(score))

    elif response.status_code == 404:
        print(Fore.RED + "\nUser not found on GitHub.")

    else:
        print(Fore.RED + "\nRequest failed.")
        print(Fore.YELLOW + "Status Code: " + str(response.status_code))