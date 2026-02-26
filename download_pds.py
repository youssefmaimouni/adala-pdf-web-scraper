import requests
import os



#output_folder = "downloaded_pdfs"
#os.makedirs(output_folder, exist_ok=True)
def download_pdf(pdf_links, output_folder):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in pdf_links:
        print(f"Downloading: {url}")

        try:
            response = requests.get(url, headers=headers, stream=True)
            response.raise_for_status()

            # Remove anchor (#toolbar=0...) from URL
            clean_url = url.split("#")[0]
            filename = clean_url.split("/")[-1]

            path = os.path.join(output_folder, filename)

            with open(path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Saved: {path}")

        except Exception as e:
            print(f"Failed to download {url}")
            print("Error:", e)

    print("Done!")