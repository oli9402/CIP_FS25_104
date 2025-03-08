# CIP_FS25_104

## Virtual Environment 
Create virtual environment by open a terminal in project folder and run: 

`python3 -m venv venv`

### Active Venv with the following command: 

Windows: 
`venv\Scripts\activate`

Mac/Linux: 
`source venv/bin/activate`

### Install Requirements 

To install all python packages in your local virtual environment run: 
`pip3 install -r requirements.txt`


### Update requirements.txt

After you install a new packages you can create an updated requirements.txt file and push it to github

`pip3 freeze > requirements.txt`


### Do not Commit Venv to Github
Add it to gitignore file so it doesn't get uploaded

`echo "venv/" >> .gitignore
git add .gitignore
git commit -m "Ignore virtual environment"
`
### Add .idea (folder setting) to gitignore
`echo ".idea/" >> .gitignore
git add .gitignore
git commit -m "Ignore PyCharm settings folder"`