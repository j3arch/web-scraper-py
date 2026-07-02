from typing import TypedDict
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup, Tag
import requests

class PageData(TypedDict):
    url: str
    heading: str
    first_paragraph: str
    outgoing_link: list[str]
    image_links: list[str]

def normalize_url(url: str) -> str:
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    h_tag = soup.find("h1") or soup.find("h2")
    return h_tag.get_text(strip=True) if h_tag else ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    main_section = soup.find("main")
    if main_section:
        first_p = main_section.find("p")
    else:
        first_p = soup.find("p")
    return first_p.get_text(strip=True) if first_p else ""



def get_urls_from_html(html: str, base_url: str) -> list[str]:
    urls = []
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all("a")

    for anchor in anchors:
        if not isinstance(anchor, Tag):
            continue
        href = anchor.get("href")
        if isinstance(href, str) and href:
            try:
                absolute_url = urljoin(base_url, href)
                urls.append(absolute_url)
            except Exception as e:
                print(f"{str(e)}: {href}")
    
    return urls


def get_images_from_html(html: str, base_url: str) -> list[str]:
    image_urls = []
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")

    for img in images:
        if not isinstance(img, Tag):
            continue
        src = img.get("src")
        if isinstance(src, str) and src:
            try:
                absolute_url = urljoin(base_url, src)
                image_urls.append(absolute_url)
            except Exception as e:
                print(f"{str(e)}: {src}")
    
    return image_urls

def extract_page_data(html: str, page_url: str) -> PageData:
    return {
        "url": page_url,
        "heading": get_heading_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
        "outgoing_links": get_urls_from_html(html, page_url),
        "image_urls": get_images_from_html(html, page_url),
    }

def crawl_page(base_url: str, current_url: str| None = None, page_data: dict[str, PageData] | None = None) -> dict[str, PageData]:
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}

    base_url_obj = urlparse(base_url)
    current_url_obj = urlparse(current_url)
    if current_url_obj.netloc != base_url_obj.netloc:
        return page_data
    
    normalized_url = normalize_url(current_url)

    if normalized_url in page_data:
        return page_data

def get_html(url: str) -> str:
    try:
        response = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
    except Exception as e:
        raise Exception(f"network error while fetching {url}: {e}")

    if response.status_code > 399:
        raise Exception(f"got HTTP error: {response.status_code} {response.reason}")

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"got non-HTML response: {content_type}")

    return response.text

def safe_get_html(url: str) -> str | None:
    try:
        return get_html(url)
    except Exception as e:
        print(f"{e}")
        return None