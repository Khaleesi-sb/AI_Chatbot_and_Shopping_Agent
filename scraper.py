import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url):
    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove things that are usually not useful for summarization
    for element in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "noscript"
    ]):
        element.decompose()

    # Get visible text
    text = soup.get_text(separator=" ", strip=True)

    return text