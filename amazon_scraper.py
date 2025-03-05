from bs4 import BeautifulSoup
import requests

URL="https://www.amazon.in/s?k=iphone+16pro+max&crid=39NRUX5DLBIF0&sprefix=%2Caps%2C874&ref=nb_sb_ss_recent_1_0_recent"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept-Language": "en-US, en;q=0.5"
}

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")



product_title = soup.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")

# Extract text inside <span> if found
if product_title:
    product_text = product_title.find("span").get_text(strip=True)
    print("Product Title:", product_text)
else:
    print("Product title not found.")
