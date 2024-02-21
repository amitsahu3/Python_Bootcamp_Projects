API key:- a tokenised password given to a user in order to track the data used 

Use of requests module to fetch data
Use of twilio Api to send text messages
use of Open weather api for weather data
pythonanywhere website for hosting the code in the web


Use of enviroment variables:

#1. convenience: setting up/deploying a big app might need to change some data a lot so use them as enviroment variables so as to keep the code untouched but change it according to the data flowing

#2. security:allows us to separately store our keys and private data from the rest of our codes 

Virtual enviroments:
    venv is created for a file or a folder only not globally , like a enviroment solely for         that project 
    # 1. after adding venv activate it
     cd venv
     cd scripts
     ls
     .\activate.ps1    (ps:powershell)
     Get-ChildItem Env:    ( list of enviroment variables)

Enviroment variables: 

are set for the enviroment and has string values an can be used in our application or code
to create enviroment vriables commands

export ENVIROMENT_VARIABLE_NAME=value

env

you can tap into this variables to do anything within the particular enviroment

in python anywhere
export OWN_API_KEY=f6fb00f88426ed19531b01bdf2037be7;export AUTH_TOKEN=7b8e8b510589078763536dc097c33f7c;python3 main.py wihile deploying/hosting


     

      
