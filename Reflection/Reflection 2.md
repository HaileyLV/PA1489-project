# **Reflections 2**

## **1. Name of everyone in the team:**
    - Ebba Bengtsson
    - Hailey Lundkvist
    - Sabor Ahmad Khowajazada
    - Thanh Chu
    - Wilma Eriksson
## **2. Link to the project's page on the git server:**
https://github.com/HaileyLV/PA1489-project.git

## **3.Assignment:**
### *3.1. Short summary of what you have implemented:*
Describe in 5–10 sentenceswhat you did and how you thought about it
#### **Sabor:**
- The project in general: We are developing an application where users can customize and place burger orders, which are then displayed in a kitchen view for preparation. The platform is split into two main applications: BurgerOrderer for customers and KitchenView for staff. These apps interact through a shared SQLite database.
- Each container: The BurgerOrderer app allows customers to customize burgers by adding or removing ingredients, choosing slides (sides), and selecting drinks.
The KitchenView app displays the incoming orders for the kitchen staff to prepare the burgers.
- Each module: Each app is built as a separate module, with its own functions for handling the customer interface and order processing.
- #### **Thanh**
- - **I have learned much during the work**. For examples: I understand a lite bit why our teacher asked us to do that:
   + a container based platform, with separate containers for BurgerOrderer, KitchenView, and MenuStore => to manage code easier and it is the reason why we need to learn how to use Docker-compose.
   + using docker and requirements => to ensure the user environment is consistent with the environment in which we build the product.
- **Short summary of what I have implemented:**
   + _The project as a whole_: I and my team work together to build two web clients that customer can order burger and people in kitchen can see the burger orders, and a database that contains information about each type of goods.
   + _Each container, each module_. What are they used for? You can know about it when you see our project's tree:
```
Containers: Our project, of course
│   ├── BurgerOrderer
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
│   ├── PA1489.egg-info: The folder and all files was automatically created when running the setup.py command
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── entry_points.txt
│   │   ├── requires.txt
│   │   └── top_level.txt
│   ├── README.md: The file with tree diagram of folders and file locations in Containers
│   ├── build: The folder and all files was automatically created when running the setup.py command.
│   │   └── bdist.macosx-10.9-universal2
│   ├── dist: The folder and all files was automatically created when running the setup.py command.
│   │   └── PA1489-0.1-py3.9.egg
│   ├── docker-compose.yaml: One for all. Run this file to define and run multi-container Docker applications.
│   └── setup.py: a central part of packaging a Python project. It defines metadata about the project (such as name, version, and author) and instructions on how to install the project and its dependencies. I copied this sentense from internet. I understand only that is's importand and helpful.
```
### *3.2. Your experiences about how the project was implemented.*
- **What went well?**
  **Thanh**
    + We have fulfilled most of the requirements of the assignment.
    + We use a single command to run the project**: docker-compose command. <docker-compose up> or <docker rmi -f customer:latest kitchen:latest && docker-compose up>
    + We have a setup.py file to define metadata about the project (such as name, version, and author) and instructions on how to install the project and its dependencies.
    + We have list types of burgers and options can see all different type as retreived from the MenuStore database. Our database is full of information, defining the types of coponents and the relationships betwwen them.
    + User can search database MenuStore contains infomation about the different type of goods and is being used by BurgerOrderer.
    + Customers can order burger, add or remove items, get the choice of options and drink. Then the order will be sent to database.  Order id is automatically numbered with function lastrowid.
    + KitchenView receives the orders, prints them and can delete them. When user delete orders in KitchenView, all information of order will be removes in database.
    + Use many try-except to catch and show errors. Customers can return to the main screen from the error screen and re-excute the transaction, the program is not interrupted.
- **What went less well?**
  **Thanh**
    + Most of our code was collected from many sources, under our efforts to learn, but there were still may limitations. Therefore, our code maybe has many duplicates, redundancies, omissions and imperfections. Howerver, we tried to do is as best as we could.
    + We don't have a good process, the division of work is not clear, so there is a lot of duplication. It took times but the efficiency was not high.
- **How did you solve the difficulties? Could you have done differently?**
  **Thanh**
    + The first challenge was that we had just started learning python when the project started. There was one team member who knew CSS and HTML. So it took us very long time to figure out what to do. Since we did not know where to start, we just coded the same functions at the same time. Then we showed it to each other and chose the best on to work on. This made the project progress very slow but we learned a bit more.
    + When we had our first product, we did not understand the assignment requirements properly so we only wrote code for one single application code for the whole product. Therefore, we had to re-edit the entire code.
    + When we finished version 2, we had to run two applications on two different text-based interfaces (iTerm and Terminal). Then we learned about Docker.
    + Finally is database. We chose SQLite instead of NoSQL because it gave us chance to pratice with database before the following courses. We spent a lot of time figuring out how many tables we needed, what the relationships were between the columns in the tables, and what joins commands we needed to use. It'difficult and confusing during working with database so we used many times command app.logger.info to print data and edited it to fit our needs.
- **What did you not manage to solve? Why not?**
  **Thanh**
    + We understod that it was not mandatory to use REST API completely for the whole project, so we used lite REST APT and the rest with Jinja2 instead. It's much more familiar, convenient and easty to learn and use for newbies like us. But we will learn about REST APT after this course.
    + There are many things we wrote that are not complete, I will come back to this exercise when I know more about programming. I guess that it will be intresting to see the lines I have coded nowaday.
    + The process. We did not have a good process. In the next project, we need to pay more attention to establishing the implementation process before starting to work.
### *3.3. Your experiences of working with containers:*
- **What went well?**
    **Thanh**
    + We learned how to work with containers and ran the produckt with two applications located in two containers BurgerOrderer and KitchenView, while the database is in MenuStore.
    + We know lite about how to buid a docker file, docker-compose and how to run it.
- **What went less well?**
  **Thanh**
    + Like I wrote above, we are new developers so out code still has many problem.
- **How did you solve the difficulties? Could you have done differently?**
  **Thanh**
    + The challenge was when the app.py files were located in two different forders and database was in MenyStore. We found a way to create vitual databases in BurgerOrderer and KitchenView and built docker images, created an automate.sh file to run one command for all. However, the problem was that the path to each person's file database was different so it did not work as we expected. We were instructed by the teacher to use docker-compose. It worked.
- **What did you not manage to solve? Why not?**
  **Thanh**
    + We tried out best to complete the assignment with the best quality with our current level. Some functions we have thougt of but dare nor risk implementing when the time for the project was not much. We may come back and implement it after this course.


