thonimport requests
from bs4 import BeautifulSoup

class ShopParser:
    def __init__(self):
        self.base_url = "https://www.etsy.com"
    
    def parse(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        shop_name = soup.find('span', class_='shop-name').get_text()
        shop_url = url
        shop_rating = soup.find('span', class_='wt-text-caption').get_text()
        shop_location = soup.find('span', class_='shop-location').get_text()
        
        shop_data = {
            'shop_name': shop_name,
            'shop_url': shop_url,
            'shop_rating': shop_rating,
            'shop_location': shop_location
        }
        
        return shop_data