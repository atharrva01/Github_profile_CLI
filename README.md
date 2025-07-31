# 🔍 GitHub User Info CLI Tool

A simple and powerful command-line tool built with Python that uses the GitHub API to fetch and display public information about any GitHub user.

## ⚙️ Features

- Takes GitHub username as input
- Displays:
  - Name
  - Profile link
  - Account type (User/Organization)
  - Followers & Following count
  - Number of public repositories
- Uses the [GitHub REST API](https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28)
- Clean and colored output with [rich](https://github.com/Textualize/rich)

---

## 🚀 How to Run

### 1. Clone the repository

git clone https://github.com/<your-username>/github-user-info-cli.git
cd github-user-info-cli

### 2. Install required libraries

pip install requests rich

### 3. Run the tool
   
python github_user_info.py --username YOUR_GITHUB_USERNAME

### EXAMPLE

python github_user_info.py --username atharrva01


### 🧠 Sample Output

This username belongs to: Atharva R.

Profile: https://github.com/atharrva01

Account Type: User

Followers: 12 | Following: 5

Public Repositories: 11


### 💡 What I Learned

Working with public APIs using Python

Parsing and handling JSON responses

Adding CLI arguments using argparse

Improving terminal UI with rich

