import os
import csv
import requests
from bs4 import BeautifulSoup
from download_pds import download_pdf
def extract_pdf_links(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a", class_="jsx-306a86c9158571de lien_plansite"):
        href = a.get("href")
        if href:
            links.append("https://adala.justice.gov.ma" + href)

    return links


def load_csv(filename):
    results = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append({'name': row.get('name'), 'link': row.get('link')})
    return results


if __name__ == "__main__":
    csv_file = "results5.csv"
    print(f"Loading entries from {csv_file}")
    entries = load_csv(csv_file)

    for entry in entries:
        name = entry['name']
        page_url = entry['link']
        print(f"\nProcessing {name}: {page_url}")

        pdf_links = extract_pdf_links(page_url)
        if not pdf_links:
            print(f"No PDF links found at {page_url}")
            continue

        folder = os.path.join("downloaded_pdfs", name)
        os.makedirs(folder, exist_ok=True)

        download_pdf(pdf_links, folder)
