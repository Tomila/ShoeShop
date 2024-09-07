import os
from flask import Flask, render_template

main = Flask(__name__)

# Dummy data for catalog
shoe_catalog = [
    {"id": 1, "name": "Sneaker X", "price": 120, "image": "sneaker_x.jpg"},
    {"id": 2, "name": "Classic Leather", "price": 100, "image": "classic_leather.jpg"},
    {"id": 3, "name": "Running Pro", "price": 130, "image": "running_pro.jpg"},
]

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/catalog')
def catalog():
    return render_template('catalog.html', shoes=shoe_catalog)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    main.run(host="0.0.0.0", port=port)
    #main.run(debug=True)






