import requests
from bs4 import BeautifulSoup

url = "https://example.com"
resp = requests.get(url, timeout=10)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
print("网页标题是：", soup.title.string)