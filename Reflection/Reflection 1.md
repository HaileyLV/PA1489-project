# **Reflections**

## **1. Name of everyone in the team:**
    - Ebba Bengtsson
    - Hailey Lundkvist
    - Sabor Ahmad Khowajazada
    - Thanh Chu
    - Wilma Eriksson
## **2. Link to the project's page on the git server:**
https://github.com/HaileyLV/PA1489-project.git

## **3.Assignment:**

### **3.1. Assignment 1:**

#### *3.1.1. Short summary about what configuration management is and why it is used:*
- _Version control system (VCS)_: we chose _Git_ as our VCS to host, manage, track and update our project. The web-based platform we used to built our product is Github, a very good platform that facilitates managing and hosting projects with Git. Moreover, Github opens for everyone, free, popular, easy to register and use, and widely supported in the industry, making it the ideal choice for our project. Besides that, Github provides tools for collaborativ development, allowing multiple people to work on projects simultaneously, by offering features like pull requests, branch management, and conflict resolution, GitHub enhances teamwork and reduces the risk of errors when merging code.
- _Application Configuration_: _Docker compose:_ Our teacher recommended Docker Compose when we had trouble running our project, where two .py files were in separate folders, and the database was in another folder. Docker Compose helps manage these multiple components (like services, databases) by defining them in a single configuration file, allowing everything to run together seamlessly.
- _Documentation Tools_: We decided to use _Markdown_, which was also recommended by our teacher, for project documentation. It is a lightweight, easy-to-learn markup language used for creating formatted text with plain text editors. Markdown is popular because it is simple, efficient, and readable in both its raw and rendered forms. Additionally, it is well-integrated with GitHub, allowing us to maintain clear and concise documentation directly within our repository. It helps us document changes, provide guidelines, create plans, write engineering diaries, and generate README files in a format that is universally recognized and recommended for clarity.

#### *3.1.2. Short summary on the most common workflow with git, including the git commands used:*
- **_With Markdown files_**: We edit directly on GitHub, which has an integrated preview feature in the editing process. GitHub offers a built-in editor with a live preview, making real-time editing and review convenient. This simplicity and integration make it our preferred choice for handling documentation files.
- **_Other files_**:
    + In our workflow, when handling tasks independently, we created branches, pushed code to them, and submited pull requests for review by all teams mebbers before merging.
        + Initially, we created three separate branches to work on. However, for various reasons, we decided to remove two of them and focus solely on the _BurgerOrderer_ branch. This branch was used to upload and modify code related to the Burger Order and Kitchen View.
        + Once we reached the database integration phase, we created a _database_ branch to continue developing the Burger Order and Kitchen View while simultaneously working on the Menu Store functionality.
        + Finally, we created a third branch when the product was nearly complete with all its core components but still needed a few feature fixes.
    + When we meet or communicate via Discord, we discuss our progress and share our achievements. Once we agree on the changes, we push them directly to the main branch. This workflow ensures smooth, organized collaboration while minimizing merge conflicts.
- **_Github command_**:
### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |

### Work with branches:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|

### Creat/remove file, forder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <forder_name]       |Create a forder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |
|-rm -rf .git                | delete all hidden files on git |


### Pull och push from local to Github:
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit mesage]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_     |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git stash pop |Apply the changes as well as remove stored files from stash area.. Link: <https://git-scm.com/docs/git-stash> _(then check git status och use git add, git commit -m, git push origin...) _  |
#### *3.1.3. Your experiences of working with configuration management:*
- **What went well?**
    + We have lerned how to get famliar with Github. Not really proficient and professional bur already know a certain number of commands related to Github, enough for our project.
    + It works very nice with Markdown. We used it a lot in the project with many filer: readme, planning, reflecktion, engineer diary...
    + When we had the first product, we put all the files in the same folder. Then we learned that we need to do two separate programs. We split them but the problem was that we needed to link the BurgerOrderer app and the KitchenView app to the database. We ran docker and an automate.sh file (to automatically run docker commands on ther terminal).  But the difficulty was that the path to the file on each machine was different. We were suggested to use _Docker Compose_. It really worked.
- **What went less well?**
    + At the beginning, we had absolutely no idea about the workload, the work sequence, and no one had enough experience to be a team leader, so we struggled to understand the project. We tried to do everything in time but we don't have a really and effective process. We need to learn about it and practice with the next project.
    + It took us a while to start using GitHub effectively. We only recently gained a better understanding of how branches work. Since we mostly meet to make decisions together, we probably encounter and resolve fewer problems than others might. For our next project, we should aim to be more proactive and engage with GitHub earlier in the process to build deeper familiarity with its features. 
- **How did you solve your challenges? What could you have done differently?**
  + The first challenge was that our team was new, and none of us had any programming experience. Faced with a project that was far beyond our skill level and imagination, we were really discouraged. We had to constantly motivate each other and work hard to learn or search for the necessary knowledge. Together, we helped each other find information, create accounts, download software, and more. By supporting each other, we felt more confident and capable.
  + We planned to meet together min two times per week but it's not working so well. Besides that, we had different circumstances so we worked at different hours and it was difficult to arrage a time to work together. Moreover, during the work, unfortunately, many of our members got sick. We changed to another ways to connect to each other: via zoom, discord, tried to write everything and push to Github so everyone can read about what we did this week, what we will do next week etc... It worked. We splited the work, worked whenever we could and everyone tried to be part of the project.
  + The next challenge was that our vision for the project was very different from reality. We drew a schematic design of a burger ordering website (check out Planning for that cool design if you're interested) and even considered details like adding ice to drinks to make the website feel more realistic. However, the implementation turned out to be too difficult. When we started working, we had little knowledge, so we had to change the design multiple times. We used Markdown files for weekly planning, documenting everything we learned so that everyone on the team could refer back to it and practice whenever they wanted—like our own project dictionary. This made things easier.
  + When we had the first product, we put all the files in the same folder. Then we learned that we need to do two separate programs. We split them but the problem was that we needed to link the BurgerOrderer app and the KitchenView app to the database. We ran docker and an automate.sh file (to automatically run docker commands on ther terminal).  But the difficulty was that the path to the file on each machine was different. We were suggested to use _Docker Compose_. It really worked.
  + The final challenge was the "Test and Debug" phase. We needed to make significant changes to our code, break it down into smaller parts, and carefully consider test cases. It was quite challenging but also very enjoyable.
- **What did you not manage to solve? Why not?**
  + We haven't fully established a proper review and commit approval process. Often, the same person who created the merge request also approved and merged the code. Additionally, we frequently pushed code directly to the remote repository and merge it into the main branch. The reasons for this are outlined in the "What went less well?" section.
  + We finished assignment 2 at the end of week 41 so we have much less time to work with Test and Debug. We had no experience with project work, so even though we have made a buget in advance of weekly plan, we are still behind schedule. In the next project, we need to calculate the plan earlier, instead of too close as it was with this project.
  
### **3.2. Assignment 2:**

#### *3.2.1. Brief summary of what you have implemented:*
Describe in 5–10 sentenceswhat you did and how you thought about it
##### **Sabor:**
- The project in general: We are developing an application where users can customize and place burger orders, which are then displayed in a kitchen view for preparation. The platform is split into two main applications: BurgerOrderer for customers and KitchenView for staff. These apps interact through a shared SQLite database.
- Each container: The BurgerOrderer app allows customers to customize burgers by adding or removing ingredients, choosing slides (sides), and selecting drinks.
The KitchenView app displays the incoming orders for the kitchen staff to prepare the burgers.
- Each module: Each app is built as a separate module, with its own functions for handling the customer interface and order processing.
- ##### **Thanh**
- - **I have learned much during the work**. For examples: I understand a lite bit why our teacher asked us to do that:
   + a container based platform, with separate containers for BurgerOrderer, KitchenView, and MenuStore => to manage code easier and it is the reason why we need to learn how to use Docker-compose.
   + using docker and requirements => to ensure the user environment is consistent with the environment in which we build the product.
- **Short summary of what I have implemented:**
   + _The project as a whole_: I and my team work together to build two web clients that customer can order burger and people in kitchen can see the burger orders, and a database that contains information about each type of goods.
   + _Each container, each module_. What are they used for? You can know about it when you see our project's tree:
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

#### *3.2.2. Your experiences about how the project was implemented.*
- **What went well?**
  **Thanh**
        + We have fulfilled most of the requirements of the assignment:
        + We use a single command to run the project**: docker-compose command. <docker-compose up> or <docker rmi -f customer:latest kitchen:latest && docker-compose up>
        + We have list types of burgers and options can see all different type as retreived from the MenuStore database. Our database is full of information, defining the types of coponents and the relationships betwwen them.
        + User can search database MenuStore contains infomation about the different type of goods and is being used by BurgerOrderer.
        + Customers can order burger, add or remove items, get the choice of options and drink. Then the order will be sent to database.  Order id is automatically numbered with function lastrowid.
        + KitchenView receives the orders, prints them and can delete them. When user delete orders in KitchenView, all information of order will be removes in database.
        + Use many try-except to catch and show errors. Customers can return to the main screen from the error screen and re-excute the transaction, the program is not interrupted.
- **What went less well?**
  **Thanh**
   + Most of our code was collected from many sources, under our efforts to learn, but there were still may limitations. Therefore, our code maybe has many duplicates, redundancies, omissions and imperfections. Howerver, we tried to do is as best as we could.
      + We only use REST API a little bit to collect the orders. The rest, we use Jinja2 instead.
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
#### *3.2.3. Your experiences of working with containers:*
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
### **3.3. Assignment 3:**
#### *3.3.1. Short summary of which functionality you have tested:*
- **Test**: I use Pytest to test with some functions som contact to the database:
#### *3.3.1. Short summary of how you have completed the test:*
    + All my test failed in the beginning because I did not set up a function to connect to the database (with 4 test) and did not use the relative path from the BurgerOrderer forder to MenuStore (with 2 test). But they were all pass after I edited the codes.
#### *3.3.2. Printout from your last test session, so you can see:*
- How many tests you have written: 6 tests
- What they test:
      + 4 test with database: I sat up a function to connect to the database in an other forder: def db_connection(), then tested if a table exist/not exist in database and test to create and drop a table in database.
      + 2 test with BurgerOrderer: tested function select_a_column and function index in BurgerOrderer. I used the relative path from the BurgerOrderer folder to MenuStore during this test.
- How many tests succeed or fail: all of them are succeed

#### *3.3.3. Your experiences about writing automated unit tests:*
- What went well?: I know how to use Pytest and could write a few test case.
- What went less well?
- How did you solve the difficulties? Could you have done differently?
    + Our functions are grouped quite a lot so testing is also more difficult. I have splitted the function to make it easier to test and I could write two test with BurgerOrderer because of it.         
- What did you not manage to solve? Why not?
    + We started with assignment 3 very late. The time was too urgent so I could not perform as many test cases as expected. In the next project, we had to adjust the time estimate.
    + I wanted to test creating and sending orders to the database but out order_id is automatically generated, so I had not dared to try, afraid of conflicts.
    + My test in BurgerOrderer are all hard-code tests. It the user changes the details in database, my tests are no longer valid. I still do nor know if there is a way to fix these things.
#### *3.3.4. Link to the documentation from your respective debug sessions in your individual engineering diarie:*
<https://github.com/HaileyLV/PA1489-project/blob/main/Engineer%20diary/Thanh%20Chu%20-%20engineer%20diary.md?plain=1>


