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
    remove_choice == ['Cheese',
                'Onion',
                'Salad',
                ]
    return render_template('options.html', remove = remove_choice)

@app.route('/confirmation')
def confirmation():
    options = ['Sauce',
                'Onion'
                ]
    if add_options () == "" and remove_options () != "":
        burger_confirm= f"1 {order()} remove {remove_options()}"
    elif add_options != "" and remove_options == "":
        burger_confirm= f"1 {order()} add {add_options()}"
    elif add_options == "" and remove_options == "":
        burger_confirm= f"1 {order()}"
    elif add_options != "" and remove_options != "":
        burger_confirm= f"1 {order(), add {add_options()}, remove {remove_options()}"  
    return render_template('confirmation.html', confirm = burger_confirm)

@app.route('/chef')
def chef():
    return render_template('chef.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
