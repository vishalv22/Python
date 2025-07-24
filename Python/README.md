# GitHub and Git 

## 🌐GitHub :
- A platform for **storing**, **sharing** and **collaborating on code**. <br>
- Uses **git** (version control) to **track code changes**.<br>
- Hosts repositories (repo) for our projects.<br>
- Feature: code storage, collaboration (pull requests), showcasing protfollios.<br><br>
- e.g., pushing my Python code to GitHub to share it and back it up.<br>
- Used by developers for **teamwork** and **opensource projects**.<br><br>

## 🛠️Git :
- A version control tool.<br>
- Runs locally in our Computers.

# 📦Setup
- Installed Git on Windows<br>
- Configured Git (Local Identity)<br>
Opened Git bash and ran :
```bash
git config --global user.name "vishalv22"
git config --global user.email "my-email"
```
This sets up my identity for all Git commits on this system.

- Created a local project folder at ```C:\Users\vishal\Desktop\Codes\Python```
- Created a new public repo called **Python** <br>
- Initialized Git Locally & Linked to GitHub
In Git Bash, navigated to the folder:
```bash
cs ~/Desktop/Code/Python
git init
```
- this linked it to the GitHub repo:
```bash
git remote add origin http://github.com/vishalv22/python.git
```
- Loged in and Done
## 📤First Push to GitHub
```bash
git add . 
#Adds all changed to the staging area

git commit -m "Intitial commit with folder structure"
#commits the changes with a message

git push -u origin main
#pushes commits to the GitHub repo
```
This uploads my local files to the GitHub repo.

## ✏️Edited Files & Pushed Again
- used same steps
```bash
git add .
git commit -m "some changes"
git push
```

## 📥Edited Directly on GitHub & Pulled
- If I or someone did some changes directly to the GitHub repo (not locally) then we can pull it and keep everything in sync :
```bash
git pull
```

