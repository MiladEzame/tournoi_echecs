# Tournoi Echecs 

**Version 1.2**


# Project Configuration

## Pull the project from github 
	
- After getting access to the github repository, pull the project with the following command :
	```python 	
	git clone https://github.com/MiladEzame/tournoi_echecs.git
	```
## Creating a virtual environment

- Python installation is required for the following process. You can download Python on python.org.
Python3 includes venv that allows us to create a virtual environment very easily.
To make sure there is no problem in the process, you can still install the virtual environment package
using this command : 
	```python 	
	pip install virtualenv
	```
	
- To create a new virtual environment called __environment_name__, write the following command line in your windows command prompt : 
	```python
	python -m venv environment_name
	```
	
## Activate/Deactivate virtual environment

- Once you've created the virtual environment, you have to activate it.
	On __Windows__, type the following command :
	```python	
	.\environment_name\Scripts\activate
	```
	On __Unix__ or __MacOS__, type the following command:
	```python 		
	source environment_name/bin/activate
	```
	If you have any difficulties, please refer to this page : https://docs.python.org/3/tutorial/venv.html
	
	Once you are done, you can simply __deactivate__ by using the following command :
	```python 		
	deactivate
	```

## Install requirement files

- Once the environment is __active__, and that you are in the Books_Scrapping folder , type this in the command prompt : 
	```python 	
	pip install -r requirements.txt	
	```
## Lauch the script 
	
- First, open the git bash inside the project folder if you are not in it.
Before running the script, make sure you are in the virtual environment.
You can run the file by using the following command :
	```python 	
	python jeu.py	
	```
## Generate a Flake 8 HTML Report :

- Begin by installing the correct package :
	```python 	
	pip install flake8-html
	```
	
	Then simply type this command line and a full report will be generated : 
	```python 	
	flake8 --format=html --htmldir=flake-report
	```

## Important information about the differents files 

- model.py
	
	This file contains all the different classes that allow us to create different instances of 
	players, tournaments, rounds and matches.

- controller.py
	
	This file makes the connexion between the views (what is seen by the user and what allows him
	to interract with the program), the model and is the main file that dictates how the whole 
	program will run.
	
- jeu.py
	
	This is the main file that launches the program.

- views.py
	
	This file allows the interaction between the user and the program. The user can use inputs to
	communicate with the program and receives outputs as answers.

- db.json
	
	This file stores all the information about our players and tournaments. It is the database that
	is used to store all the informations.

- random_players.txt
	
	This is a file that allows the creation of 8 random players and their informations if the program
	needs to be tested quickly. 

- requirements.txt
	
	This file contains all the modules needed to run this program properly. You can use it as described
	in the install requirements file section.

## Contributors 

- Milad EZAME <milad.ezame@gmail.com>
- © Milad EZAME - OpenClassrooms 
