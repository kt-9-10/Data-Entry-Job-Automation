import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"


class ZillowController:

    def __init__(self):
        response = requests.get(URL)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def get_list_of_links(self):
        links = [link.get("href") for link in self.soup.select(".property-card-link")]
        return links

    def get_list_of_prices(self):
        prices = [price.get_text() for price in self.soup.select(".PropertyCardWrapper span")]
        replaced_prices = []
        for price in prices:
            replaced_prices.append(price.split("+")[0].split("/")[0])
        return replaced_prices

    def get_list_of_address(self):
        # print(self.soup)
        addresses = [address.get_text() for address in self.soup.find_all(name="address")]
        replaced_addresses = []
        for address in addresses:
            replaced_addresses.append(address.replace("  ", "").replace("\n", "").replace("| ", ""))
        return replaced_addresses
