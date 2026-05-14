from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(url):
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

def get_first_paragraph_from_html(html):
    pass



def get_heading_from_html():
    pass

def get_urls_from_html():
    pass