# GitHub User Info Tool

A simple command-line tool to fetch and display basic information about a GitHub user account and their public repositories.

## Features

- Displays user profile information (name, followers, following, public repos count)
- Shows account type and profile URL
- Lists the top 5 public repositories with details:
  - Repository name
  - Programming language
  - Clone URL
  - Creation date
  - Last updated date
- Clean, colorized output using Rich library

## Requirements

- Python 3.6+
- `requests` library
- `rich` library

## Installation

1. Clone or download the script
2. Install required dependencies:

```bash
pip install requests rich
```

## Usage

Run the script from the command line with a GitHub username:

```bash
python github_info.py --username <github_username>
```

### Example

```bash
python github_info.py --username octocat
```

### Sample Output

```
This username belongs to The Octocat
View the complete profile of The Octocat, here https://github.com/octocat
This account is public
octocat has 4000 Followers & he follows to 9 accounts
The user has 8 Public Repository

1. Hello-World
Languages: None
Repo Url. https://github.com/octocat/Hello-World.git
Repo Created on 2011-01-26T19:01:12Z
Repo Last Updated on 2011-01-26T19:14:43Z

2. Spoon-Knife
Languages: HTML
Repo Url. https://github.com/octocat/Spoon-Knife.git
Repo Created on 2011-01-27T19:30:33Z
Repo Last Updated on 2011-01-27T19:30:33Z
```

## Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--username` | Yes | GitHub username to fetch information for |

## Error Handling

- The script will display "Not Provided" if any profile information is unavailable
- Network errors and invalid usernames will cause the script to fail - consider adding error handling for production use

## API Rate Limits

This tool uses the GitHub REST API without authentication, which has a rate limit of 60 requests per hour per IP address. For higher rate limits, consider adding GitHub token authentication.

## Notes

- Only displays public repositories
- Shows a maximum of 5 repositories
- All data is fetched from GitHub's public API
- The script uses colorized output via the Rich library for better readability

## License

This tool is provided as-is for educational and personal use.
