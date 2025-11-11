## Features

- Search products by keywords or URLs.
- Scrape detailed product and shop information.
- Export data to JSON files.

## Configuration

You can modify the settings in `src/config/settings.example.json`.

## Example Output

The scraper will produce output like this:

```json
[
{
"product_name": "Handmade Silver Necklace",
"product_url": "https://www.etsy.com/listing/123456789/handmade-silver-necklace",
"price": "$35.00",
"reviews": [
{"rating": "5", "comment": "Beautiful necklace! Exactly as described."},
{"rating": "4", "comment": "Lovely item but took longer to arrive."}
],
"shop_name": "The Silver Studio",
"shop_url": "https://www.etsy.com/shop/TheSilverStudio",
"shop_rating": "4.8",
"category": "Jewelry",
"product_image_url": "https://www.etsy.com/images/necklace.jpg"
}
]