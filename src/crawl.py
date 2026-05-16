from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(url):
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

def get_heading_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    h_tag = soup.find("h1") or soup.find("h2")
    return h_tag.get_text(strip=True) if h_tag else ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    main_section = soup.find("main")
    if main_section:
        first_p = main_section.find("p")
    else:
        first_p = soup.find("p")
    return first_p.get_text(strip=True) if first_p else ""



def get_urls_from_html():
    pass


def get_urls_from_html(html, base_url):
    urls = []

    return urls

def extract_page_data(html, page_url):
    return {
        "url": page_url,
        "heading": get_heading_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
    }
