# **Reflections 1**

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
