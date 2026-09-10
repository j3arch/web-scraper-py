from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url: str) -> str:
    parsed_url = urlsplit(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

def get_heading_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    h_tag = soup.find("h1") or soup.find("h2")
    return h_tag.get_text() if isinstance(h_tag, Tag) else ""

def get_first_paragraph_from_html(html):
    pass

