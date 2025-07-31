import requests
import argparse
from rich import print

parser = argparse.ArgumentParser(description="This is a tool to get basic info of the account by enetering the username")
parser.add_argument("--username" , required=True , help="Enter the Github Username")
args = parser.parse_args()

username = args.username

url = f"https://api.github.com/users/{username}"
repos_url = f"https://api.github.com/users/{username}/repos"

data = requests.get(url).json()
repos_data = requests.get(repos_url).json()

length_repo = int(len(repos_data))

name = (data["name"])


complete_profile = data["html_url"]

ac_type = data["user_view_type"]


followers = data["followers"]
following = data["following"]

repos = data["public_repos"]


if (name or complete_profile or ac_type or followers or following or repos) == "None":
        print("Not Provided")

else:
        print(f"This username belongs to [yellow]{name}")
        print(f"View the complete profile of [yellow]{name}, [white]here [yellow]{complete_profile}")
        print(f"This account is [yellow]{ac_type}")
        print(f"[yellow]{username} [white]has [yellow]{followers} [white]Followers & he follows to [yellow]{following} [white]accounts")
        print(f"The user has [yellow]{repos} [white]Public Repository")






for i,repo in enumerate(repos_data[:5],1):
        Repo_name = repo["name"]
        Repo_created = repo["created_at"]
        Repo_updated = repo["updated_at"]
        Clone_repo = repo["clone_url"]
        Visibility = repo["visibility"]
        Forks = repo["forks"]
        language = repo["language"]

        print(f"\n{i}.[green]{Repo_name}")
        print(f"Languages: {language}")
        print(f"Repo Url. {Clone_repo}")
        print(f"Repo Created on {Repo_created}")
        print(f"Repo Last Updated on {Repo_updated}")
        print()
