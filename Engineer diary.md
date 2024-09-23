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
| Command s                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>              |

### Work with branches:
| Command s                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |              

### Creat/remove file, forder on main/branches
| Command s                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file (on local)      |
|mkdir <forder_name]       |Create a forder (on local)      |
|git rm [file_name.py]                   |remove a file (local)                                       |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem    |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem      |
| git add [file_name.py]                    | add a python file to the staging area (on local)      |
| git add -A                 | add all new and changed files to the staging area (on local)         |


### Pull och push from local to Github:
| Command s                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local (if you did not add a file to the staging area, this file will be in red text  |
|git commit -m "[commit mesage]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit**        |
|git push origin main                       | push your local content to GitHub (main)                   |
|git push origin <branch's name> | push your local content to GitHub (branch)  |
|Solve problem when using pushing code to Github but the previous pull code is not the latest version |   
|git log |You need to read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
## Week 39:
### 1. Solve problem when using pushing code to Github but the previous pull code is not the latest version:
See section "Pull och push from local to Github" - week 38

## Week 40:
- 
## Week 41:
- 
## Week 41:
- 
## Week 42:
- 
## Week 43:
- 
## Week 44:
-

**• Try to get into the habit of often thinking through what you have done, what you
learned, and what you need to find out.
• Rather write a little every day than a lot once a week.
• Don't forget to commit what you wrote so that it appears in the project log.**
