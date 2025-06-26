# Fetch the HTML (requests)
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)

# Parse HTML (BeautifulSoup)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the Headlines
Headlines = soup.find_all('h2')
for i, h in enumerate(Headlines, start=1):
    title = h.text.strip()
    if title:  # Check if title is not empty    
        print(f"{i}. {title}")

# Save Headlines to a File
with open('headlines.txt', 'w') as file:
    for h in Headlines:
        title = h.text.strip()
        if title:  # Check if title is not empty
            file.write(title + '\n')