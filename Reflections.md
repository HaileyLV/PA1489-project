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
- _Version control system_: we chose _Github_ to host, manage, track and update our project. The reason is because it opens for everyone, free, popular, easy to register and use. Besides that, Github provides tools for collaborativ development, allowing multiple people to work on projects simultaneously.
- _Documentation tools_: we use _Markdown_. It's also easy to use, free and recommended by the teacher.
#### *3.1.2. Short summary on the most common workflow with git, including the git commands used:*
- With Markdown file: we edit directly on Github. Github has integranted Preview directly in the editing process. It's very convenient, so we prefer to use it that way.
- Other files: during the working process, when we work independently based on the assigned task, we create some branches, push code to them and send merge pull requests to other colleagues. When we meet or contact each other via Discord, we discuss and show each other our achievements. The things we have shown and agreed on, we push directly to the main.
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
- **What went well?** We have lerned how to get famliar with Github. Not really proficient and professional bur already know a certain number of commands related to Github, enough for our project.
- **What went less well?** It took us a long time to start using Github. We only recently got a better understanding of how branches work. We mostly meet to make decisions, so we probably encounter and deal with fewer problems than others. We should be more hands-on in out next project.
- **How did you solve your challenges? What could you have done differently?**
  + The first challenge was that our team was new. No one had any programming experience. Faced with a project that was far beyond our level and imagination, we were really discouraged. We needed to always encourage each other and try to learn or find the necessary knowledge.
  + The next challenge was that our imagination of the project was too different from reality. We drew a schematic design of a burger ordering website (look in _Planning_ to see that super cool design if you want), thinking about whether to add ice or not to the dinks to make the wedsite look like reality, but to implement it was too difficult. When we started working, we didn't know anything so we had to change the design many times.
  + When we had the first product, we put all the files in the same folder. Then we learned that we need to do two separate programs. We split them but the problem was that we needed to link the BurgerOrderer app and the KitchenView app to the database. We ran docker and an automate.sh file (to automatically run docker commands on ther terminal).  But the difficulty was that the path to the file on each machine was different. We were suggested to use _Docker Compose_. It really worked.
- **What did you not manage to solve? Why not?** We haven't really created a review and commit approval flow. The person who creates the merge request is often the same person who submits the code merge. We also often push code directly to remote and merge it into main branch. The reasons ad we mentioned in the _"What went less well?"_. 

### **3.2. Assignment 2:**

#### *3.2.1. Brief summary of what you have implemented:*
Describe in 5–10 sentenceswhat you did and how you thought about it
- The project in general
- Each container
- Each module

#### *3.2.2. Your experiences about how the project was implemented.*
- What went well?
- What went less well?
- How did you solve the difficulties? Could you have done differently?
- What did you not manage to solve? Why not?

#### *3.2.3. Your experiences of working with containers:*
- What went well?
- What went less well?
- How did you solve the difficulties? Could you have done differently?
- What did you not manage to solve? Why not?

### **3.3. Assignment 3:**

#### *3.3.1. Brief summary of which functionality you have tested:*

#### *3.3.1. Brief summary of how you have completed the test:*

#### *3.3.2. Printout from your last test session, so you can see:*
- How many tests you have written
- What they test
- How many tests succeed or fail

#### *3.3.3. Your experiences about writing automated unit tests:*
- What went well?
- What went less well?
- How did you solve the difficulties? Could you have done differently?
- What did you not manage to solve? Why not?

#### *3.3.4. Link to the documentation from your respective debug sessions in your individual engineering diarie:*



