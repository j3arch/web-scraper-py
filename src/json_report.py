import json
from crawl import PageData

def write_json_report(page_data: dict[str, PageData], filename: str ="report.json") -> None:
    if not page_data:
        print("No data to write to JSON")
        return