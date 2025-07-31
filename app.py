import requests
import argparse
from rich import print

parser = argparse.ArgumentParser(description="This is a tool to get basic info of the account by enetering the username")
parser.add_argument("--username" , required=True , help="Enter the Github Username")
args = parser.parse_args()

username = args.username
url = f"https://api.github.com/users/{username}"

data = requests.get(url).json()

if data.status_code != 200:
    print(f"[red]❌ Error: Couldn't fetch data for '{username}'. Please check the username and try again.")
    exit()

name = (data["name","N/A"])
print(f"This username belongs to [yellow]{name}")

complete_profile = data["html_url","N/A"]
print(f"View the complete profile of [yellow]{name}, [white]here [yellow]{complete_profile}")

ac_type = data["user_view_type","N/A"]
print(f"This account is [yellow]{ac_type}")

followers = data["followers",0]
following = data["following",0]
print(f"[yellow]{username} [white]has [yellow]{followers} [white]Followers & he follows to [yellow]{following} [white]accounts")

repos = data["public_repos",0]
print(f"The user has [yellow]{repos} [white]Public Repository")

