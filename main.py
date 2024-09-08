import os
import secrets
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime, timedelta
from flask_mail import Mail, Message

main = Flask(__name__)

# Generate and set a secure secret key
main.secret_key = secrets.token_hex(16)

# Configure Flask-Mail for Windows Live (Outlook.com)
main.config['MAIL_SERVER'] = 'smtp.office365.com'
main.config['MAIL_PORT'] = 587  # Port for TLS
main.config['MAIL_USERNAME'] = 'tomilaine@windowslive.com'  # Replace with your Windows Live email
main.config['MAIL_PASSWORD'] = 'ViiviPumpanen89'  # Replace with your Windows Live email password
main.config['MAIL_USE_TLS'] = True  # Use TLS
main.config['MAIL_USE_SSL'] = False  # Do not use SSL
main.config['MAIL_DEFAULT_SENDER'] = 'tomilaine@windowslive.com'  # Replace with your Windows Live email

mail = Mail(main)

# Dummy data for catalog with special offers
shoe_catalog = [
    {
        "id": 1,
        "name": "Sneaker X",
        "price": 120,
        "image": "sneaker_x.jpg",
        "description": "A sleek and comfortable sneaker perfect for all-day wear.",
        "sale_price": 100
    },
    {
        "id": 2,
        "name": "Classic Leather",
        "price": 100,
        "image": "classic_leather.jpg",
        "description": "Elegant leather shoes for a timeless look.",
        "sale_price": 85
    },
    {
        "id": 3,
        "name": "Running Pro",
        "price": 130,
        "image": "running_pro.jpg",
        "description": "High-performance running shoes with superior cushioning.",
        "sale_price": 110
    },
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

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/contact_submit', methods=['POST'])
def contact_submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('All fields are required.')
            return redirect(url_for('contact'))

        # Create and send the email
        msg = Message('Contact Form Submission',
                      recipients=['tomilaine@windowslive.com'],  # Replace with recipient email
                      body=f"Message from {name} ({email}): {message}")
        try:
            mail.send(msg)
            flash('Thank you for your message! We will get back to you soon.')
        except Exception as e:
            flash('An error occurred while sending your message.')
            print(f"Error: {e}")

        return redirect(url_for('contact'))

    return render_template('contact.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    main.run(host="0.0.0.0", port=port)








