jupyter_notebook:
1. create a new github repository ex. jupyter_notebook
2. create a empty python file ex. jupyter.py
3. clone the github repository to repl.it ("import repo")
4. @.replit file, replace ' run =  "" ' with ' run = "jupyter notebook --ip=0.0.0.0 --port=3000" '
5. type these in terminal(in order):
   a. pip install --upgrade pip
   b. pip install notebook
   c. (jupyter --version ← if you want to check)
   d. jupyter notebook --generate-config
   e. jupyter notebook password
6. Enter and confirm the password
7. click the "Run" button and here you go
Ps. if you want to save them back to github:
1. git init
2. git add .
3. (git status ← if you want to check)
4. git commit -m "<anything>"
5. git push -u origin master