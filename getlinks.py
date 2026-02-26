import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://adala.justice.gov.ma/resources/1"  # base site URL
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []

for a in soup.find_all("a", href=True):
    href = a["href"]

    if href.startswith("/resources/"):
        span = a.find("span")
        if span:
            name = span.get_text(strip=True)
            full_url = urljoin(url, href)

            results.append({
                "name": name,
                "link": full_url
            })

import csv

for r in results:
    print(r)

# save results to csv
csv_file = "results5.csv"
with open(csv_file, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "link"])
    writer.writeheader()
    writer.writerows(results)

print(f"Saved {len(results)} entries to {csv_file}")