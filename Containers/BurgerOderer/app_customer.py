#import the functions required
from flask import Flask, render_template, request, redirect, url_for
from flask_menu import Menu, register_menu
import sqlite3

app = Flask(__name__)
Menu(app=app)

# Set up the database: sqlite
def init_db():
    """_summary_
    """
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders 
                 (id INTEGER PRIMARY KEY, customer_name TEXT, burger TEXT, added_items TEXT, removed_items TEXT, drink TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
@register_menu(app, '.', 'Home')
def index():
    return render_template('index.html')

# Collect the order. 
# If customer don't add any items, print "No slides".
# If customer don't want to remove any topping, print "Full topping"
@app.route('/order', methods=['POST'])
def place_order():
    customer_name = request.form['name']
    burger = request.form['burger']
    added_items = request.form.getlist('added_items')
    removed_items = request.form.getlist('remove_items')
    drink = request.form['drink']

    added_str = ', '.join(added_items) if added_items else 'No slides'
    removed_str = ', '.join(removed_items) if removed_items else 'Full topping'

    # Save order in the database
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders (customer_name, burger, added_items, removed_items, drink) VALUES (?, ?, ?, ?, ?)",
              (customer_name, burger, added_str, removed_str, drink))
    conn.commit()
    conn.close()

    return redirect(url_for('index')) 

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=8000)