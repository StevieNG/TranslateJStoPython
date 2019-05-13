# TranslateJStoPython
A demo task to "translate" a program which convert .csv to .json from Java Script to Python 

**Requirment** :
1) On a html file, user to select a csv file to be converted 
2) csv file to be loaded, arranged, and appended to two list: nodes and edges
3) Create 2 json files (nodes and edges) with current time stamp as file name 

**Approach:**

intitially "data.py" was created as a python shell program to get the main functionalities to work

then "dataFlask.py" was created to use Flask framwork to link the function to an user interface on a html file - "index.html"

**Instruction?  (more like note to self)**

data.py - to be run as $python3 data.py

dataFlask need the Flask framework in a virtual enivirmeint 
 
$python3 -m venv venv
$source venv/bin/activate
$export FLASK_APP=dataFlask.py
$flask run

$deactivate  to stop
