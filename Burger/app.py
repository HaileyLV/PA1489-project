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
                (id INTEGER PRIMARY KEY, customer_name TEXT, burger TEXT, added_items TEXT, removed_items TEXT, added_sides TEXT, drink TEXT)''')
    conn.commit()
    conn.close()


# Route för hemsidan (index)
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


@app.route('/order_done', methods=['POST'])
def done():
    form_data = request.form
    print(form_data)

    customer_name = request.form['name']
    burger = request.form['burger']
    print(burger)
    add_items = request.form.getlist('add_items')
    print(add_items)
    removed_items = request.form.getlist('remove_items')
    print(removed_items)
    added_sides = request.form.getlist('added_sides')
    print(added_sides)
    drink = request.form['drink']
    print(drink)
    add_items = ",".join(add_items)
    removed_items = ",".join(removed_items)
    added_sides = ",".join(added_sides)

    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO orders (customer_name, burger, added_items, removed_items, added_sides, drink)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (customer_name, burger, add_items, removed_items, added_sides, drink))

    conn.commit()
    conn.close()

    return render_template('order_done.html')


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)