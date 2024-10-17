v.35 walk-through:
Introduction about the course.
instructions we need to do this coming 2 weeks: 
Build a group with 3 to 5 people. 

I created a group with Hailey. for the next week we are trying to get 1 or more members in it. 
We need to be atleast 3 people. 

Set up my computer for the courses. 
Created a github account.

36 
What happend:

#Went through the innerworking and otherworkig of mjukvara.

This week we found 3 more people that needed to be in a group.
So we created a 5 members group together.

Created a group on discord so we could hold contact. 

Meeting 1:
We introduce ourself to the team, got to kow each other a little.
Hailey created a project on Github and shared it to everyone.

We desided to split the project up:

mainmanu: 
Sabor

burgerorder:
hamburger (thanh)

choices (ebba & hailey)

sides (wilma)

kitchen view:
Sabor
(thanh)


37-38
What i lernd: 
markdown, app.moqups, flask.

Lear about necessary material that need to know: Github,



how to get github to ure terminal:
ssh key


git init -> Initialize a local Git repository
git clone <git@github.com:HaileyLV/PA1489-project.git> Creat a local copy on your computer. Read more: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
----

----
Github command:
git checkout -b <branch's name> creat a branch or move to the branch

git checkout - jump between two branches

git branch -> check all the branches on local

git branch --delete <branch's name> delete branch on local 

git branch -a -> Confirm Git branch deletion

git push origin --delete -> Remove a remote Git branch
----

----
touch <file name] -> Create a python file (on local)

mkdir <folder name] -> Create a folder (on local)

git rm [file name] -> remove a file _(local) _

git rm file name -> To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _

git rm file name --cached -> To remove the file from the repository, but keep it on the filesystem (when file has been pushed to Github)

git add [file name] -> add a python file to the staging area _(on local) _

git add -A -> add all new and changed files to the staging area (on local) (not recommended because it can lead to commiting/pushing unsued files)
----

----
git pull -> pull code from remote to local (must do this every time before starting anything)

git status -> check status in local (if you did not add a file to the staging area, this file will be in red text. if added its going to be green)

git commit -m "[commit message (short comprehensible summary of change!)]" -> commit changes . Commit message is for other people to get a short summery on what was commit.

A branch is for project/ work where more then one is working on the project. Its to make it easier for the group to work on the project together.
Usually one or two people works on one branch with one specific part of the project. When that part is completed you can send a request for the other people in the group
to check if they think it looks good and everything works together. After that you can push the branch to main without having any problems that it dose not fit in with the other work.

If you don't have a branch´s, its can be complected to push what you have done to main. It may interfere with things that others users have submitted without you nowing about it. 
Sometimes maybe two people have done the same thing.  


git push origin main -> push your local content to GitHub (main -> were the main project is)

git push origin <branch's name> push your local content to GitHub (branch)

(Solve problem when using pushing code to Github but the previous pull code is not the latest version.)

git log -> 	Read and check the difference between local and remote

git reset --soft HEAD~1 -> Reset current HEAD to the specified state. Link: https://git-scm.com/docs/git-reset

git stash -> Stash the changes in a dirty working directory away. Link: https://git-scm.com/docs/git-stash

git fetch -> Stash the changes in a dirty working directory away. Link: https://git-scm.com/docs/git-stash

git stash pop -> Apply the changes as well as remove stored files from stash area.. Link: https://git-scm.com/docs/git-stash _(then check git status och use git add, git commit -m, git push origin...) _
----

#Solve problem when using pushing code to Github but the previous pull code is not the latest version: See section "Pull och push from local to Github"
Issue: the Deleted BurgerOrderer (BO) branch directly from the Github screen without reading the message from the terminal window. 
This resulted in the BO branch on the local but not on the remote, user lost connection with the remote and could not pull or push the code. 
Solution: evaluated that user did not use this branch locally, so user deleted it locolly and pulled from Github again. 
Lear more how to delete a branch on local and on remote. See section "Work with branches"


V.37 
            learn:

#Learn about product design.

---

            WHat happen in the group:

We agree in the group to use programming language (Python), environment (VS code) gitserver (Github) 
(this was pre-decided)

We decided to focuses this week on to learn about python! We didn't have enough information to start yet about the program jet. 

In our discord group, one of the member wanted to change how we were going to divided the work. 
The member wanted to do everything together. I sad that we could talk about it together next time we are together.

----
            What i did:

Set up Github for terminal use:
Set up a SSH key:
In the terminal, type the following command, replacing youremail@example.com with your email address (the same one you use for GitHub):
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"

In order for your SSH key to be used automatically by Git, you need to add it to your SSH agent.
Start SSH-agent-> 
eval "$(ssh-agent -s)"

Add your SSH key to the SSH agent: 
ssh-add ~/.ssh/id_rsa

Copy the public SSH-key and add it to GitHub.
cat ~/.ssh/id_rsa.pub
Copy the entire key showing in terminal.

Go to GitHub:
Log in on your GitHub-account.
Go to SSH and GPG keys- settings.
Click on New SSH key.
Give key a name (example "My computer (lenovo)") and paste the key you copied from the terminal into the Key field.
Click Add SSH key.
(now you have added your own specified code, 
that acts like a log in for when you work in a project.
It is to know that you are you when you commit things in a project at Github.)

To test if it worked:
ssh -T git@github.com
if correct set up: Hi username! You've successfully authenticated, but GitHub does not provide shell access. (in terminal)

Now you can clone, push and pull via SSH. 
To clone a repository, use SSH-link instead of HTTPS:
git clone git@github.com:username/repository.git

Github:
Set the SSH keys to Github. Come to Settings -> SSH and GPG key Link https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account and https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

You only need one SSH-key, so you probably only need to do this once.

-----
v.38 
            Learn:
Learn about Flask and download the software.
Practice pulling and pushing data from each person's computer to Github. (created my own github project so i would not disturb our project)
Code BurgerOrderer and KitchenView

hshs

            What happen in the group:

When we meet upp next time for a meeting. 
Two of the group members hade done almost the whole burger-order. 
We hade not decided this according to me. What we hade decided was to wait another week before we do something on the project.
Just so we hade enough information to start doing the burger-oder together. 

They told us that we could do:
Make burger-order be able to remove item from burger.

next week I had done my own github order so i could show them how w could do it. 
but when they should oss what they hade done. they hade arady done it

            What i did:

install Flask using the following command in terminal:
pip install Flask
Verify the Installation:
python -m flask --version
Learn about Flask and download the software. Link: https://flask.palletsprojects.com/en/3.0.x/installation/.

How i learn about flask: 
Learn about Flask commands to create a simple application. Link: https://www.geeksforgeeks.org/flask-creating-first-simple-application/

---
Created my own Burger-app 
made a running website. 
Used wsl, html and pip flask. 

v.39
            learn:
Learn about Flask. Link: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
Code BurgerOrderer and KitchenView, write documents.
Update Engineer diary

            what happen in the group:
Work together with team to release BurgerOrderer (BO) and KitchenView (KV) version 1 and 2.



            What i did:
download flask-menu:
pip install Flask-Menu
Verify the Installation:
pip list | grep Flask-Menu
if correct-> Flask-Menu (0.7)

Download and use FLask-Menu to code. Link https://flask-menu.readthedocs.io
----
Install Docker:
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
Download and try to learn how to use Docker Desktop. Link https://www.docker.com/products/docker-desktop/

Install Docker Desktop (windows):
Invoke-WebRequest -Uri https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe -OutFile DockerDesktopInstaller.exe

Docker commands:
docker build -t <image's name>: . -> Build dockers images. Best att use ex: customer: lastest'for the images name and version
docker images -> Show all images
docker run -d --name -p <image's name>: -> run the docker image

running container stop or start:
docker stop adminer
docker start adminer
----
In my own hade burger order i did a database and docker file. sent it upp to github so everyone could see, 
and take som inspiration for our project. 

----

v40
            learn:
whats the difference between docker file and docker compose.
If you have download docker file you hade automatically Docker compose. So no downloading.
Adminer is for so you can go in your database and change staff there.

            What happen in the group:
Product assembly and testing the first time
Code MenuStore and write document of MenuStore
Practice:
Did not finish with MenuStore. Need to learn about Docker-compose and Dababase.
Did not do any test or fix any bug


            What i did:

#Virtual machine skriv hur man gör commands 
vad command gör:


Download Adminer with docker:
docker run --name adminer -d -p 8080:8080 adminer
Access Adminer in your browser: Open your browser and navigate to http://localhost:8080.

running container stop or start:
docker stop adminer
docker start adminer

----
change my burger-order docker file to a docker compose. 
This was because with a docker compose file you can run through all 3 docker files. 
with docker file you need to open up all there every time. With compose it just runs a lot smother.
created a kitchen view.

v41
            learn:

            What happen in the group:

Need to:
TEST OCH DEBUG:
Read about "Testing Flask applications with pytest" and try to doing it by yourself
We will forst test that the input data on the order website is sent to kitchenview. You are welcome to do more tests if you want.
Please tell everyone if you find a bug that needs to be fixed before you change any code.
Document everything when working. Check 11-pages of Mikael to have the right structure.
Finished the lastest Monday night.
ASSIGNMENT 2
Write yourself first and we will meet on Tuesday to write everything together.
Fell free to create an .md file on Github type: thanh-reflection and write there.
            
            What i did:
Finish with database and Docker-compose file.
Test, fix bug, write document about exercise 1,2,3

----
SQLite commands:

CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);
->
Create a table named test, if it was not exists in database with two elements: id and name.

DROP TABLE IF EXISTS test; -> Drop a test table if it was exists in database

SELECT name FROM sqlite_master WHERE type = 'table' AND name='test';
->
Check the positions of table if it exists in database. Returns None if the table does not exist in the database

select * from burger b join order_burger ob on b.id = ob.burger_id join orders o on ob.order_id = o.id join items i on ob.items_id = i.id where o.id = ?
->
Join data in table burger with tabler order_burger, table items with table order_burger based on burger_id, order_id, items_id

INSERT INTO burger (id, name) VALUES (1, "cheese burger")
->
Insert a row in table burger with two elements: id = 1 and name = cheese burger

('SELECT id FROM items WHERE name = ? AND type = ? AND action = ?',(item_name, item_type, action))
->
pull data of item_name, item_type, action based on items_id

('INSERT INTO order_burger (order_id, burger_id, items_id) VALUES (?, ?, ?)',(order_id, burger_id, item_id))
->
insert input data to database

with sqlite3.connect('orders.db') as conn:...
->
use this code to open database so that database will be closed outside "with"


Docker-compose file
------


----

fixed a list for my burger-order so I can add more burgers if i want to the order.
Put in order error in docker compose file. 

v42
Finish with document
Check all again before submit

Use pytest to test and debug: link: https://docs.pytest.org/en/stable/getting-started.html
Finish with engineer diary
Check all things and submit submissions

Need to set up logging. Very helpful for debug. Print out to console with command: app.logger.info("Burger: %s", burger). Don't need to write ""Burger: %s"," but it's easier to read when it have many row will be printed to console.
Run pytest from terminal: pytest
Use "@pytest.fixture" for beginning a function if want to define a reusable setup for testing
A test function start with "test"
----
debugging 
fixt las on txt 

reflektion: 
 challenger: working togheter, not being abol to commit.
 good: aducationol, we tried to help echoder with the projekt.
 next: more struktusre. everybody has thire on thing to do!
