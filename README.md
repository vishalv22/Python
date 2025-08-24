# Git and GitHub 

## <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30"> GitHub

- A platform for **storing**, **sharing** and **collaborating on code**. <br>
- Uses **git** (version control) to **track code changes**.<br>
- Hosts repositories (repo) for our projects.<br>
- Feature: code storage, collaboration (pull requests), showcasing protfollios.<br><br>
- e.g., pushing my Python code to GitHub to share it and back it up.<br>
- Used by developers for **teamwork** and **opensource projects**.<br><br>

## 🛠️ Git :
- A version control tool.<br>
- Runs locally in our Computers.

# 📦 Setup
- Installed Git on Windows<br>
- Configured Git (Local Identity)<br>
Opened Git bash and ran :
```bash
git config --global user.name "vishalv22"
git config --global user.email "my-email"

 #This configures Git with my name and email for commit authorship.
```
This sets up my identity for all Git commits on this system.

- Created a local project folder at ```C:\Users\vishal\Desktop\Python```
- Created a new public repo called **Python** <br>
- Initialized Git Locally & Linked to GitHub
In Git Bash, navigated to the folder:
```bash
cs ~/Desktop/Python
git init
```
- this linked it to the GitHub repo:
```bash
git remote add origin http://github.com/vishalv22/python.git
```
- Loged in and Done
## 📤 First Push to GitHub
```bash
git add . 
#Adds all changes to the staging area

git commit -m "Intitial commit with folder structure"
#This creates a commit - a snapshot of the current changes with a message.

git push -u origin main
#pushes commits to the GitHub repo
```
This uploads my local files to the GitHub repo.

## ✏️ Edited Files & Push Again
used same steps
```bash
git add .
git commit -m "message"
git push
```

## 📥 Edited Directly on GitHub & Pull
If I or someone did some changes directly to the GitHub repo (not locally) then we can pull it and keep everything in sync :
```bash
git pull
```
<br>

## 🌿 What is git Branch?
- it is like a copy of our codebase where we can make changes without affecting the main version.
- ```main``` (or ```master```) is the dafault branch.
```bash
git checkout -b backup-main
```
<br>

- It made a copy of our current project state, named ```backup-main``` and switch to it. 
- If we made important work in ```backup-main``` and want to bring it to ```main```: <br>
Switch to ```main``` branch first (```git checkout main```) --> then merge the branch (```git merge backup-main```)
<br>

## 🫴🏻 Using touch command
```touch``` simply used to creat a new, empty file in the current folder, example ```touch hello.py``` or ```touch readme.md``` <br>
it's just a quick way to create any empty file.
<br>

## ✏️ Editing and Rewriting Commits in Git

### Edit last commit message
To edit last commit message, Run:
```bash
git commit --amend
```
Change message and save.
Then force push the updated commit to GitHub:
```bash
git push --force
```
### Rewriting Entire Commit History
We can squash, edit, or reorder all commits starting from the root commit by using interactive rebase with ```--root```. <br>
Useful for cleaning up commit history before sharing the repo.
<br>

Example :

```bash
git rebase -i --root
```
- Replace ```pick``` with ```squash``` or ```edit``` for each commit as needed.
- Save and follow Git's prompts.

### Git Commit on Past Dates
We can set the commit date manually using the ```--date``` flag. Useful for adding missed commits with the correct timeline.
<br>
Example :

```bash
git commit --date='2025-08-08' -m "message"
```

## Unicode?

- **Unicode** is a standard that assigns a unique number (called *code point*) to every character in every language and symbol set.  
  - Example: `'A' → 65`, `'a' → 97`, `'क' → 2325`.

- In Python, characters are compared based on their **Unicode code points**, not the "dictionary order" we use in daily life.  
  - `'A' < 'a'` because 65 < 97.  

- Functions like `min()`, `max()`, and sorting use these numeric values to compare strings.  

- We can find the Unicode value of a character using:  
  ```bash
  ord('A')   # 65
  ord('a')   # 97
  ord('क')   # 2325
  ```
  
- And we can convert a Unicode number back to a character with:
  ```bash
  chr(65)    # 'A'
  chr(2325)  # 'क'
  ```
