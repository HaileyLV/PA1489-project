#import the functions required
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Set up the database: sqlite
def init_db():
    """_summary_
    """
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS orders 
                 (id INTEGER PRIMARY KEY, customer_name TEXT, burger TEXT, added_items TEXT, removed_items TEXT, added_slides TEXT, drinks TEXT)''')
    conn.commit()
    conn.close()

# Route for home side (index)
@app.route('/')
def index():
    return render_template('main_menu.html')

@app.route('/cheese')
def cheese():
    return render_template('cheese_burger.html')

@app.route('/fish')
def fish():
    return render_template('fish_burger.html')

@app.route('/vegan')
def vegan():
    return render_template('vegan_burger.html')

# Collect the order. 
# Default: No add items, Full topping, No slides, No drinks
@app.route('/order_done', methods=['POST'])
def done():
    form_data = request.form
    print(form_data)
    
    customer_name = request.form.get('name', None)
    if customer_name:
        print(f"Customer Name: {customer_name}")
    else:
        print("No customer name provided.")
        
    burger = request.form['burger']
    print (burger)
    added_items = request.form['added_items']
    print(added_items)
    removed_items = request.form['removed_items']
    print(removed_items)
    added_slides = request.form['added_slides']
    print(added_slides)
    drinks = request.form['drinks']
    print(drinks)
    

    # Save order in the database
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO orders (customer_name, burger, added_items, removed_items, added_slides, drinks)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (customer_name, burger, added_items, removed_items, added_slides, drinks))

    conn.commit()
    conn.close()

    return render_template('order_done.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000, debug=True)