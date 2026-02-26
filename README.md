# PDF Web Scraper and Downloader

An automated tool to scrape legal resource links from the Moroccan Justice Portal and download associated PDF documents.

## Overview

This project automates the process of:
1. **Extracting resource links** from the Moroccan Justice Administration website (adala.justice.gov.ma)
2. **Finding PDF documents** associated with each resource
3. **Downloading PDFs** to organized local folders

## Project Structure

### Files

- **`getlinks.py`** - Web scraper that extracts resource links from the main page
  - Targets: https://adala.justice.gov.ma/resources/1
  - Outputs: `results5.csv` with resource names and URLs

- **`main.py`** - Main orchestration script
  - Loads resource URLs from CSV file
  - Extracts PDF links from each resource page
  - Creates organized folders and triggers downloads

- **`download_pds.py`** - PDF downloader module
  - Downloads PDF files from URLs
  - Handles request errors gracefully
  - Saves files with original names in specified folders

- **`results*.csv`** - CSV files containing scraped resource data
  - Columns: `name`, `link`

- **`downloaded_pdfs/`** - Output directory containing downloaded PDFs organized by resource

## Requirements

```
requests
beautifulsoup4
```

## Installation

1. Install dependencies:
```bash
pip install requests beautifulsoup4
```

2. Ensure you have Python 3.6+ installed

## Usage

### Step 1: Extract Resource Links
```bash
python getlinks.py
```
This will scrape the main resources page and save links to `results5.csv`.

### Step 2: Download PDFs
```bash
python main.py
```
This will:
- Load URLs from `results5.csv`
- Extract PDF links from each resource page
- Download all PDFs to `downloaded_pdfs/<resource_name>/`

## Notes

- User-Agent headers are included to avoid blocking by the website
- PDFs are organized in folders named after each resource
- Failed downloads are logged with error messages
- Anchor tags (#toolbar=0, etc.) are removed from PDF URLs before saving
- Existing downloads are not re-downloaded; new folders are created as needed

## Error Handling

- Network errors are caught and reported
- Missing or invalid links are skipped
- Failed downloads don't stop the entire process

## Output

Downloaded PDFs are saved in the following structure:
```
downloaded_pdfs/
├── Resource Name 1/
│   ├── document1.pdf
│   └── document2.pdf
├── Resource Name 2/
│   └── document3.pdf
└── ...
```
