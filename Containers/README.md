# Each container, each module. What are they used for? You can know about it when you see our project's tree:
```
Containers: Our project, of course
│   ├── BurgerOrderer: 
│   │   ├── BO_test.py: File test for modul app.py
│   │   ├── Dockerfile: To built and run a customer's image
│   │   ├── app.log: File we have after set up logging to debug. We use commands: app.logger.info many times during working to print. It's very helpful to debug.
│   │   ├── app.py: A back-end file? We built it to take information from database, collect orders and sent orders to database
│   │   ├── requirements.txt: All needed applications to ensure the program runs in the same environment as when we built the product.
│   │   └── templates: All front-end files for Burger Order
│   │       ├── error.html: Error screen during execution. We put a lot of try-except to catch errors and throw it to the error screen. Here, the customer can press return to the main screen and start over. The program will be not crash by it.
│   │       ├── index.html: Simple CSS to make the home page a little nicer.
│   │       ├── main_menu.html: Burger order page. When the customer clicks on the burger type, the information is temporarily saved, the home page switches to the topping page for the customer to continue choosing the toppings and options for the burger.
│   │       ├── topping.html: Customer choose options to burger. The customer can return to the previous page by clicking the "Go back" button and "Submit" to sumbit the order.
│   │       └── order_done.html: After the customer clicks submit in the topping page, the burger information and options are collected and sent to the database. The order notification page has been collected. The customer order more py clicking the "Click here if you want to order more" button.
│   ├── KitchenView
│   │   ├── Dockerfile: To built and run kitchen's image
│   │   ├── app.py: A back-end file to Kitchen. It used to receive infomation from database and print on the customer scrren.
│   │   ├── requirements.txt: All needed applications to ensure the program runs in the same environment as when we built the product.
│   │   └── templates
│   │       └── kitchen.html: The kitchen can view orders or delete them if desired
│   ├── MenuStore
│   │   ├── db_test.py: test database with pytest
│   │   ├── orders.db: database with SQLite (we used DB Browser for SQLite to built it)
│   │   └── orders.sqbpro: A executable file rendered by DB Browser for SQLite to when we use it to built database
│   └── docker-compose.yaml: One for all. Run this file to define and run multi-container Docker applications.
```
## **You need to run docker-compose to define and run multi-container Docker applications.**