# importing libraries

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1.  Scrape the links, addresses, and prices of the rental properties (USING BEAUTIFULSOUP)

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
data = response.text
soup = BeautifulSoup(data, 'html.parser')

# list of all the links on the page (using a CSS Selector)
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
#print(f"There are {len(all_links)} links to individual listings in total: \n")

# list of all the addresses on the page (using a CSS Selector)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
#print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
#print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")

#2 - Fill in the Google Form (USING SELENIUM)

# keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    # TODO: Add fill in the link to your own Google From
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScoND_vqgMa4Ko8ybU1dUAhJJ_Sjihl2KBIY0OKntLHjPFXMg/viewform?usp=sf_link")
    time.sleep(2)

    # Use the xpath to select the "short answer" fields in your Google Form.
    # Note, your xpath might be different if you created a different form.
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()