thonimport json
from extractors.product_parser import ProductParser
from extractors.shop_parser import ShopParser
from outputs.data_exporter import DataExporter

def main():
    # Example URLs for product and shop scraping
    product_url = 'https://www.etsy.com/listing/123456789/handmade-silver-necklace'
    shop_url = 'https://www.etsy.com/shop/TheSilverStudio'
    
    # Parse product details
    product_parser = ProductParser()
    product_data = product_parser.parse(product_url)
    
    # Parse shop details
    shop_parser = ShopParser()
    shop_data = shop_parser.parse(shop_url)
    
    # Export scraped data
    data_exporter = DataExporter()
    data_exporter.export(product_data, 'product_data.json')
    data_exporter.export(shop_data, 'shop_data.json')
    
if __name__ == '__main__':
    main()