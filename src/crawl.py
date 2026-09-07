from urllib.parse import urlsplit

def normalize_url(url: str) -> str:
    parsed_url = urlsplit(url)
    full_path = f"{parsed_url.netlock}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

