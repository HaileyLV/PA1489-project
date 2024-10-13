# **This is the programmer diary I write every week**

## Content in file:
- .1. Summaries of the work
   + a. The things I have done every week:
   + b. The things I have learned every week
- .2. My thinking about:
   + a. Collaboration
   + b. Configuration management
   + c. Implementation and documentation
   + d. Testing and debugging
   
## 1. Summaries of the work
### a. The things I have done every week: (update planning, engineer diary)
#### Week 35+36: 



#### Week 37:



#### Week 38:


#### Week 39



| Version 1                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use buttons to save orders| Use check-boxes to temporarily record the user's choice |
|The order is recorded after each click so user can not change their choices | The order is only actually saved when user click on "Order Now" button so they can make change before this action|
|It is possible to move bach and forth between BO and KT through the "Go to kitchen" and "Back to order" links. BO and KV 2 parts of 1 program. | BO and KV are 2 separate programs that point to the database _(set up with hardcode, not yet complete)_|
|The kitchen receives all orders in an unnumbered list | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|
|The kitchen can delete allorder data all order data but can not delete individual orders || 
|The product design model will be changed. It is expected to try to do so that the add_items and remove_items are attributes in the buger.||
- Learn about using a virtual machine

- 
#### Week 40:



  
#### Week 41:



| Version 3                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use dropdown lists to temporarily store user selections. Menus pulled from database. Have actual database files with tables and relations.| Use check-boxes to temporarily record the user's choice. Menu is only hard code. Database had been created by manual code in .py file, had no tables or relations |
|The orders will be sent to the database and save to tables | The order will be sent to the database file without tables|
|The kitchen receives the beautiful order with all information | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|
- Database with help by DB browser for SQLite
- Rewrited Docker-compose file, Docker file and Requirments: add database and pytest

  
#### Week 42:



### b. The things I have learned every week:
#### Week 35 - 39:


  
##### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |

##### Work with branches:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|

##### Creat/remove file, forder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <forder_name]       |Create a forder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |

##### Pull och push from local to Github:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit mesage]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_                   |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git stash pop |Apply the changes as well as remove stored files from stash area.. Link: <https://git-scm.com/docs/git-stash> _(then check git status och use git add, git commit -m, git push origin...) _  |
- Solve problem when using pushing code to Github but the previous pull code is not the latest version: See section "Pull och push from local to Github" 
- **Issue:** the Deleted BurgerOrderer (BO) branch directly from the Github screen without reading the message from the terminal window. This resulted in the BO branch on the local but not on the remote, user lost connection with the remote and could not pull or push the code. Solution: evaluated that user did not use this branch locally, so user deleted it locolly and pulled from Github again. Lear more how to delete a branch on local and on remote. See section "Work with branches" 
#### Week 40:
 - Virtual machine
**- How to activate virtual machine from terminal/iTerm...with Mac:**
  
| Commands                                  | To do                                             |
| ----------------------------------------- | ------------------------------------------------- |
|cd <path to navigate to the virtual machine installed directory>. Ex: on my laptop: <cd myproject/.venv/bin> With your laptop, it can be diffirence| move to the virtual machine installed directory|
|soucre activate | turn on the virtual machine|
- Can make an automate.sh to run the docker file more quickly without type every lines in terminal. Run automate.sh with commands: ./automat-run.sh
- Docker commands:

 |Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|docker build -t <image's name>:<version> .| Build dockers images. Best att use ex: customer: lastest'for the images name and version  |
|docker images | Show all images|
|docker run -d --name <containers name> -p <ports> <image's name>:<version> | run the docker image|
#### Week 41:
- SQLite commands:
  
|Commands                                 | To do                                                |
| ----------------------------------------- | -------------------------------------------------  |
|CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT); | Create a table named test, if it was not exists in database with two elements: id and name.|
|DROP TABLE IF EXISTS test; | Drop a test table if it was exists in database |
|SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';| Check the positions of table if it exists in database. Returns None if the table does not exist in the database |
|select * from burger b join order_burger ob on b.id = ob.burger_id join orders o on ob.order_id = o.id join items i on ob.items_id = i.id where o.id = ? |Join data in table burger with tabler order_burger, table items with table order_burger based on burger_id, order_id, items_id |
|INSERT INTO burger (id, name) VALUES (1, "cheese burger") | Insert a row in table burger with two elements: id = 1 and name = cheese burger|
|('SELECT id FROM items WHERE name = ? AND type = ? AND action = ?',(item_name, item_type, action)) | pull data of item_name, item_type, action based on items_id|
|('INSERT INTO order_burger (order_id, burger_id, items_id) VALUES (?, ?, ?)',(order_id, burger_id, item_id))|insert input data to database|
|with sqlite3.connect('orders.db') as conn:...|use this code to open database so that database will be closed outside "with"|
- Docker-compose file

  
#### Week 42:



### 2. My thinking about:
#### a. Collaboration:
**- Chalenges:** 

**- What went well:** We planned to meet together min two times per week but it's not working so well in the beginning. We have different circumstances. As I need to take care of my family so I usually study from 8-12, 13-15 and 20-23. During the work, unfortunately, many of our members got sick. We changed to another way to connect to each other with another ways: via zoom, discord. I tried to write everything and push to Github so everyone can read about what we did this week, what we will do next week etc... It worked. We splited the work, worked at different times and everyone tried to be part of the project.

**- What need to change next time** We had absolutely no idea about the workload, the work sequence, and no one had enough experience to be a team leader, so we struggled to understand the project. I think each of us learned certain lessons after this project. With me, the most important things need to do first is the process. 

#### b. Configuration management
- **About Github**:

  
- **And Markdown**:

  
- **About docker-compose**:


#### c. Implementation and documentation:


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

4. Your experiences of conducting the project.
• What went well: we leared a new thing everyday. It's so hard 
• What did not go well?
• How did you solve your challenges? What could you have done dif-
ferently?
• What did you not manage to solve? Why not?
5. Your experiences of working with containers.
• What went well?
• What did not go well?
• How did you solve your challenges? What could you have done dif-
ferently?
• What did you not manage to solve? Why not?

#### d. Testing and debugging


##### what is being debugged, the breakpoints used, the variables monitored and how these change during the debug session. There are reflections on what went well (or not), with identified opportunities for improvements.


