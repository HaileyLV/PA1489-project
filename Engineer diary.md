# **This is the programmer diary we write together every day, every week**

## Week 35+36: 
  - Learn about Github.
  - Create Github accounts and GitHub repo. Link: <https://github.com/HaileyLV/PA1489-project.git>
## Week 37:
- Learn about md syntax. Link: <https://www.markdownguide.org/basic-syntax/>
- Draw a draft design <https://app.moqups.com/CNsCqWOjxAXBnT1q7BVJIuRvwCjqD6zl/view/page/ad64222d5>
## Week 38:
- Learn about Flask and download the software. Link: <https://flask.palletsprojects.com/en/3.0.x/installation/>.
- Set the SSH keys to Github. Come to Settings -> SSH and GPG key Link <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account> and <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>
- Flask commands to create a simple application. Link: <https://www.geeksforgeeks.org/flask-creating-first-simple-application/>
- Github command:
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


### Pull och push from local to Github:
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


## Week 39:
- Solve problem when using pushing code to Github but the previous pull code is not the latest version: See section "Pull och push from local to Github" - week 38
- **Issue:** the Deleted BurgerOrderer (BO) branch directly from the Github screen without reading the message from the terminal window. This resulted in the BO branch on the local but not on the remote, user lost connection with the remote and could not pull or push the code. Solution: evaluated that user did not use this branch locally, so user deleted it locolly and pulled from Github again. Lear more how to delete a branch on local and on remote. See section "Work with branches" -week 38.
- Download and use FLask-Menu to code. Link <https://flask-menu.readthedocs.io>
- Virtual machine
**- How to activate virtual machine from terminal/iTerm...with Mac:**
  
| Commands                                  | To do                                             |
| ----------------------------------------- | ------------------------------------------------- |
|cd <path to navigate to the virtual machine installed directory>. Ex: on my laptop: <cd myproject/.venv/bin> With your laptop, it can be diffirence| move to the virtual machine installed directory|
|soucre activate | turn on the virtual machine|
Learn more why we need to use a virtual machine in Mikael's virtual machine lecture#7.
- Release _BurgerOrderer (BO) and KitchenView (KV)_ version 1 and 2.
  
| Version 1                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use buttons to save orders| Use check-boxes to temporarily record the user's choice |
|The order is recorded after each click so user can not change their choices | The order is only actually saved when user click on "Order Now" button so they can make change before this action|
|It is possible to move bach and forth between BO and KT through the "Go to kitchen" and "Back to order" links. BO and KV 2 parts of 1 program. | BO and KV are 2 separate programs that point to the database _(set up with hardcode, not yet complete)_|
|The kitchen receives all orders in an unnumbered list | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|
|The kitchen can delete allorder data all order data but can not delete individual orders                                                                         || 
|The product design model will be changed. It is expected to try to do so that the add_items and remove_items are attributes in the buger.                        ||

## Week 40:
- Download and try to learn how to use Docker Desktop. Link <https://www.docker.com/products/docker-desktop/>
- Download Docker compose
- Download Adminer
## Week 41:
| Version 3                                 | Version 2                                         |
| ----------------------------------------- | ------------------------------------------------- |
|Use dropdown lists to temporarily store user selections. Menus pulled from database. Have actual database files with tables and relations.| Use check-boxes to temporarily record the user's choice. Menu is only hard code. Database had been created by manual code in .py file, had no tables or relations |
|The orders will be sent to the database and save to tables | The order will be sent to the database file without tables|
|The kitchen receives the beautiful order with all information | Orders are managed by customer name _(need to check if programs crashes when customer have the same name)_|
- Database with help by DB browser for SQLite
- Docker-compose file
## Week 42:
- Use pytest to test and debug: link: <https://docs.pytest.org/en/stable/getting-started.html>
- 
**• Try to make a habit of thinking through what you have done, what you
learned, and what you need to find out.
• It's better to write a little every day than a lot once a week.
• Don't forget to commit what you have written so that it appears in the project log.**
