# import all needed functions
from flask import Flask, render_template, redirect, url_for
import sqlite3
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def view_orders():
    """Display all orders received from the app."""
    try:
        with sqlite3.connect('orders.db') as conn:
            cursor = conn.cursor()
            # Insert order and get order_id
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            result = list()
            app.logger.info(orders)
            # join tables, create result list that content information of the order: order_id, burger name, items name etc...
            for order in orders:
                app.logger.info(order[0])
                
                # retrieve data by joining several related tables (burger, order_burger, orders, and items) based on common keys 
                # such as order_id, burger_id, items_id
                cursor.execute("select * from burger b join order_burger ob on b.id = ob.burger_id \
                    join orders o on ob.order_id = o.id join items i on ob.items_id = i.id \
                        where o.id = ?", (order[0],))
                items = cursor.fetchall()
                app.logger.info(items)
                result_item = list()
                result_item.append(order[0])
                result_item.append(order[1])
                for item in items:
                    result_item.append(item[9])
                    result_item.append(item[10])
                    result_item.append(item[11])
                result.append(result_item)
            app.logger.info(result)
    
    # Handle database errors (optional: log the error, show a message, etc.)        
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        orders = []  # Return an empty list in case of an error
    return render_template('kitchen.html', result=result)

@app.route('/delete_orders', methods=['POST'])
def delete_orders():
    """Delete all orders from the database."""
    try:
        with sqlite3.connect('orders.db') as conn:
            cursor = conn.cursor()
            
            # Delete all records from order_burger table
            cursor.execute("DELETE FROM order_burger")
            app.logger.info("All records from 'order_burger' deleted successfully.")
            
            # Delete all records from orders table
            cursor.execute("DELETE FROM orders")
            app.logger.info("All records from 'orders' deleted successfully.")
            
            # Commit the changes
            conn.commit()
    except sqlite3.Error as e:
        app.logger.error(f"Failed to delete orders: {e}")
    return redirect(url_for('view_orders'))  # Redirect to the orders page after deletion

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8001)