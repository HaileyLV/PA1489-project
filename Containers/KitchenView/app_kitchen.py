# import all needed functions
from flask import Flask, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Kitchen received the orders from app_customer and shows the detail
@app.route('/')
def view_orders():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("SELECT customer_name, burger, added_items, removed_items, drink FROM orders")
    orders = c.fetchall()
    conn.close()
    return render_template('kitchen.html', orders=orders)

# Persons in kitchen can delete all orders. Information of removed orders has been deleted in database.
@app.route('/delete_orders', methods=['POST'])
def delete_orders():
    """Delete all orders from the database."""
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    c.execute("DELETE FROM orders")
    conn.commit()
    conn.close()
    return redirect(url_for('view_orders'))  # Redirect to the index or orders page after deletion

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)