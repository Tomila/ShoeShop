import os
from flask import Flask, render_template
from datetime import datetime, timedelta

main = Flask(__name__)

# Dummy data for catalog with special offers
shoe_catalog = [
    {"id": 1, "name": "Sneaker X", "price": 120, "sale_price": 90, "image": "sneaker_x.jpg"},
    {"id": 2, "name": "Classic Leather", "price": 100, "sale_price": 70, "image": "classic_leather.jpg"},
    {"id": 3, "name": "Running Pro", "price": 130, "sale_price": 100, "image": "running_pro.jpg"},
]

# Flash sale duration and end time
flash_sale_duration = timedelta(hours=4)
flash_sale_end = datetime.now() + flash_sale_duration  # Flash sale for 4 hours

# Sample news data
news_items = [
    {"title": "New Winter Collection Released!", "date": "2024-09-01", "content": "Check out our latest winter collection!"},
    {"title": "Free Shipping for Orders Over $100", "date": "2024-09-03", "content": "Enjoy free shipping when you spend more than $100."},
]

@main.route('/')
def index():
    # Pass flash_sale_end and news_items to the template
    return render_template('index.html', shoes=shoe_catalog, flash_sale_end=flash_sale_end, news_items=news_items)

@main.route('/catalog')
def catalog():
    return render_template('catalog.html', shoes=shoe_catalog)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    main.run(host="0.0.0.0", port=port)








