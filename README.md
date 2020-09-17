# RESTful_API

A simple web app using the Amazon RDS Oracle database to serve information using a RESTfull API with basic authentication.

## Technologies
### Languages
Python 3.8.2
### Frameworks
Flask 1.1.2
### Databases
Oracle AWS RDS Standard Edition 2 Release 19.0.0.0.0 - Production
Version 19.7.0.0.0



## Instructions on Running the Code

I have developed and run the code on Ubuntu 20.04.1 LTS. Should you wish to run the code on a different OS please take care to make sure that the packages in use are supported on the different systems.

The first step is to copy the code to a local directory to be run, this can be achieved by running the following git command:  
git clone <https://github.com/Alexandru-S/RESTful_API.git>  

Once the code is cloned to your directory a virtual environment will need to be created to store the python packages we are using.  
This can be achieved by running the following commands in the command line:  
##### if virtualenv is not present in the system already
> pip install virtualenv    
##### create a python3 virtual environment
> virtualenv --python python3 env3
##### activate the environment  
> source env3/bin/activate
##### install all the required packages
cd RESTful_API  
> pip install -r requirements.txt

After all the packages have been succesfully installed in the system we can go ahead and run the application by executing the following commands:  
##### run the application  
> python main.py 
##### stop the application  
> CTRL + C 
###### exit the virtual environment  
> deactivate




note about <https://restcountries.eu/rest/v2/name/irl?fullText=true> format not working, thus needing to use the <https://restcountries.eu/rest/v2/alpha?codes={code1};{code1};{code1}> format  
note about needing to use a better method than calling an api to convert country codes to countrys names
note about regparse deprecation <https://flask-restful.readthedocs.io/en/latest/reqparse.html>