from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orders = []


@app.route('/')
def index():
    return render_template('index.html')  


@app.route('/kitchen')
def kitchen_view():
    return render_template('kitchen.html', orders=orders)  

@app.route('/order', methods=['POST'])
def order():
    item = request.form['item']  
    orders.append(item)  
    return redirect(url_for('index'))  


@app.route('/clear_orders')
def clear_orders():
    orders.clear() 
    return redirect(url_for('kitchen_view')) 


if __name__ == '__main__':
    app.run(debug=True)

