from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
TARGET_PRICE = 100

dummy_endpoint = "https://appbrewery.github.io/instant_pot/"
live_endpoint = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept-Language": "en-US,en;q=0.5", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0"
}

response = requests.get(live_endpoint, headers=headers)
website_data = response.text
soup = BeautifulSoup(website_data, "html.parser")

price_data = soup.find(name="span", class_="aok-offscreen").getText()
price_split = price_data.split("$")
price_float = float(price_split[1])

item_title = soup.find(name="span", class_="a-size-large product-title-word-break", id="productTitle").getText()
item_title_formatted = " ".join(item_title.split())
# item_title_formatted = " ".join(item_title.split()).encode('ascii', 'ignore').decode('ascii')

if price_float < TARGET_PRICE:

    with smtplib.SMTP(f"{SMTP_ADDRESS}", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ENTER RECIPIENT EMAIL ADDRESS",
            msg=f"Subject:Price Reduction Alert!\n\n{item_title_formatted} is now ${price_float}\n{live_endpoint}".encode('utf-8')
        )
