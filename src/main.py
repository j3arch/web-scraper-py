import sys
from crawl import get_html

def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]
    print(f"starting crawl of: {base_url}...")

    try:
        html = get_html(base_url)
    except Exception as e:
        print(f"Error fetching HTML from {base_url}: {str(e)}")
        sys.exit(1)

    print(html)
    sys.exit(0)
    
if __name__ == "__main__":
    main()
