# **In this text I'll be updating progress, problems I've encountered and solutions along with other things I've learned in this course.**

## Things about the text
- Text is divided into two parts
    1. My work throughout the weeks
    2. Thoughts about the project and how it went


## 1. My work throughout the weeks
#### Week 35 and 36: 

    - Created a group of five people (Myself, Ebba, Wilma, Thanh, Sabor).
    - Learned about Git and Github (https://www.youtube.com/watch?v=mJ-qvsxPHpY)
        Note: Also touched on the topic of branches.
    - Created Github account and GitHub repo (https://github.com/HaileyLV/PA1489-project.git)
    - Planed and structured how the work should be distributed. 



#### Week 37:
    - Watched videos and read about md syntax (https://www.markdownguide.org/basic-syntax/)
    - Created SSH key for Github
    - Group agreed and decided to divide parts of the project and assign it to smaller groups. (Ex. two people do KitchenView.)


#### Week 38:
    - Researched about Flask and installed the program.
    - Two people in the group strayed from the original plan of dividing the project into sections, and did almost the whole project on their own. 
        Note: Concerned about not being able to partake in the project.
    - Group member took my computer and I was confused on what they were trying to do. (This later caused issues in committing things to the project.)
        Note: Don't let others do things on your computer if you are unaware what they are doing.
    - Learned different git commands.
    - Downloaded Docker desktop (https://www.docker.com/products/docker-desktop/).

| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|git pull                   | pull code from remote to local (**must do this every time before starting anything**)
|git status                                | check status in local _(if you did not add a file to the staging area, this file will be in red text)_  |
|git commit -m "[commit message]"           | commit changes . **Always need to type the commit message for everyone know about what's the new things in your commit** |
|git push origin main                       | push your local content to GitHub _(main)_                   |
|git push origin <branch's name> | push your local content to GitHub _(branch)_  |
|*Solve problem when using pushing code to Github but the previous pull code is not the latest version*||   
|git log |Read and check the difference between local and remote   |
|git reset --soft HEAD~1 |Reset current HEAD to the specified state. Link: <https://git-scm.com/docs/git-reset> |
|git stash |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |
|git fetch |Stash the changes in a dirty working directory away. Link: <https://git-scm.com/docs/git-stash>   |

#### Week 39

    - Expanded my knowledge with branches 
    - Try to catch up and find something I can work on the project.
        Note: Was given instructions to do debugging (though never got to do that since that one teem member decided to do that too).
    - Downloaded Docker compose.
    - Downloaded Adminer. 
    - Read about what docker was and installed the program. 
    - Start to understand the concept of what a container is. (Tried doing one by myself.)

| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git checkout -b <branch's name>             | creat a branch or move to the branch    |
| git checkout -                            | jump between two branches                       |    
| git branch                           | check all the branches on local                    |
| git branch --delete <branch's name>  | delete branch on local                  |
|git branch -a|Confirm Git branch deletion|
|git push origin --delete|Remove a remote Git branch|


#### Week 40:
    - Downloaded Docker desktop (https://www.docker.com/products/docker-desktop/).
    - Downloaded Docker compose.
    - Downloaded Adminer. 
    - Read about what docker was and installed the program. 
    - Start to understand the concept of what a container is. (Tried doing one by myself.)

#### Week 41:
    - Started with my own database using MySQL.
    - Trying to do my own take on the project
        Side note: Have been trying to structure the work from the beginning, however one of the members seems to do the project by herself without including the rest of the group. Talked to her and thought wew were on the same page until she eventually did the thing she said I should do. Decided to do my project on the side to show my understanding.
    - Test & Debug - Check if vscode can run and debug more than one file and if it can see whether the files work together or not - It can debug more than one only you might need extensions to see if the files work together (not sure if it works for this project however).
        Note: Ended up using pytest to see if it works.

#### Week 42:
    - Finish with engineer diary
    - Check all things and submit submissions


### Commands I learned but don't remember when I learned them

    - All the commands below are from notes taken during the project.  

  
##### Start with Github
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
| git init                                    | Initialize a local Git repository     |
| git clone <git@github.com:HaileyLV/PA1489-project.git> |Creat a local copy on your computer. Read more: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>   |



##### Create/remove file, folder 
| Commands                                 | To do     |
| ----------------------------------------- | ------------------------------------------------- |
|touch <file_name.py]       |Create a python file _(on local_)      |
|mkdir <folder_name]       |Create a folder _(on local)_      |
|git rm [file_name.py]                   |remove a file _(local) _                                      |
|git rm file_name.py.txt         | To remove a file both from the Git repository and the filesystem _(when file has been pushed to Github) _   |
|git rm file_name.py --cached  |  To remove the file from the repository, but keep it on the filesystem _(when file has been pushed to Github)_ |
|git add [file_name.py]                    | add a python file to the staging area _(on local) _     |
|git add -A                 | add all new and changed files to the staging area _(on local)_ **(not recommended because it can lead to commiting/pushing unsued files)**  |



  
| Commands                                  | To do                                             |
| ----------------------------------------- | ------------------------------------------------- |
|cd <path to navigate to the virtual machine installed directory>. Ex: on my laptop: <cd myproject/.venv/bin> With your laptop, it can be diffirence| move to the virtual machine installed directory|
|source activate | turn on the virtual machine|
- Can make an automate.sh to run the docker file more quickly without type every lines in terminal. Run automate.sh with commands: ./automat-run.sh
- Docker commands:

 |Commands                                 | To do                                      |
| ----------------------------------------- | ------------------------------------------------- |
|docker build -t <image's name>:<version> .| Build dockers images. Best att use ex: customer: latest for the images name and version  |
|docker images | Show all images|
|docker run -d --name <containers name> -p <ports> <image's name>:<version> | run the docker image|
