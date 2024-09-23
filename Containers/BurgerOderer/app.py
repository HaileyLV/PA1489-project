from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def order():
    burgers_order = ['Burger 90 gram',
                'Burger 160 gram',
                'Vegatarian burger'
                ]
    return render_template('index.html', order = burgers_order)

@app.route('/addoptions')
def add_options():
    add_choice = ['Cheese',
                'Bacon',
                'Halloumi',
                ]
    return render_template('options.html', add = add_choice)

@app.route('/removeoptions')
def remove_options():
    remove_choice = ['Cheese',
                'Onion',
                'Salad',
                ]
    return render_template('options.html', remove = remove_choice)

@app.route('/confirmation')
def confirmation():
    order_choice = order() 
    add_choice = add_options()  
    remove_choice = remove_options() 

   
    if not add_choice and remove_choice:
        burger_confirm = f"1 {order_choice} remove {remove_choice}"
    elif add_choice and not remove_choice:
        burger_confirm = f"1 {order_choice} add {add_choice}"
    elif not add_choice and not remove_choice:
        burger_confirm = f"1 {order_choice}"
    else:
        burger_confirm = f"1 {order_choice}, add {add_choice}, remove {remove_choice}"

    return render_template('confirmation.html', confirm = burger_confirm)

@app.route('/chef')
def chef():
    return render_template('chef.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
<<<<<<< Updated upstream
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> Stashed changes
