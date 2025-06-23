import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the trending page
url = 'https://github.com/trending'
headers = {'User-Agent': 'Mozilla/5.0'}  # Prevent blocking
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find repository entries
repo_tags = soup.find_all('h2', class_='h3 lh-condensed')[:5]  # Top 5

# Step 4: Extract names and links
trending_repos = []
for tag in repo_tags:
    anchor = tag.find('a')
    repo_name = anchor.get_text(strip=True).replace('\n', '').replace(' ', '')
    repo_link = 'https://github.com' + anchor['href']
    trending_repos.append([repo_name, repo_link])

# Step 5: Save to CSV
with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['repository name', 'link'])  # Header
    writer.writerows(trending_repos)

print("Top 5 trending repositories saved to 'trending_repos.csv'")
