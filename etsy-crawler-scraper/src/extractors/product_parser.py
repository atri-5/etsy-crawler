thonimport requests
from bs4 import BeautifulSoup

class ProductParser:
    def __init__(self):
        self.base_url = "https://www.etsy.com"
    
    def parse(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_name = soup.find('h1', class_='wt-text-body-03').get_text()
        product_url = url
        price = soup.find('span', class_='currency-value').get_text()
        reviews = self.get_reviews(soup)
        shop_name = soup.find('span', class_='shop-name').get_text()
        shop_url = soup.find('a', class_='shop-name')['href']
        shop_rating = soup.find('span', class_='wt-text-caption').get_text()
        category = soup.find('span', class_='wt-badge').get_text()
        product_image_url = soup.find('img', class_='wt-image')['src']
        
        product_data = {
            'product_name': product_name,
            'product_url': product_url,
            'price': price,
            'reviews': reviews,
            'shop_name': shop_name,
            'shop_url': shop_url,
            'shop_rating': shop_rating,
            'category': category,
            'product_image_url': product_image_url
        }
        
        return product_data
    
    def get_reviews(self, soup):
        reviews = []
        review_elements = soup.find_all('div', class_='wt-list-unstyled')
        for review in review_elements:
            rating = review.find('span', class_='star-rating')['aria-label']
            comment = review.find('p', class_='wt-text-truncate').get_text()
            reviews.append({'rating': rating, 'comment': comment})
        return reviews