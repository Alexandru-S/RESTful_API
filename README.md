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
`git clone https://github.com/Alexandru-S/RESTful_API.git `

Once the code is cloned to your directory a virtual environment will need to be created to store the python packages we are using.  
This can be achieved by running the following commands in the command line:  
> if virtualenv is not present in the system already  
`pip install virtualenv`

> create a python3 virtual environment  
`virtualenv --python python3 env3`

> activate the environment  
`source env3/bin/activate`

> install all the required packages  
`cd RESTful_API  `  
`pip install -r requirements.txt`

After all the packages have been successfully installed in the system we can go ahead and run the application by executing the following commands:  
> run the application  
`python main.py`

> stop the application  
You need to click on the command line that is running the web app and click `CTRL + C `

> exit the virtual environment  
`deactivate `

## Running the application in Localhost
Add Explanation  here

## Feature Explanations

###Departments

#### GET /department
Going to the /department endpoint will returns back all the department table rows in JSON format.
No more features were asked to be added for this endpoint so none more were added, although there is a possibility for expansion.

### Badges

#### GET /badges/active
This endpoint will retrieve back all (**BADGE_STATUS** == active) **AND** (**BADGE_EXPIRY_DATE** > datetime.date.today())
As per the instruction provided.  
Should no badges be active a **404 error** message will be returned.  

#### GET /badges?badge_number=[badge_number]
Only the badge number that matches the query parameter will be returned, if it exists.  
If it doesn't exist a 404 error will be returned.  
If the format is malformed or not matching specifications a **422 error** will be returned by the reqparse add_argument() function.

As the above example, no more options were added due to none more being asked at this endpoint but there is room for expansion.

### Job Titles

#### GET /job_titles
Returns all job titles as per requirements.

### Employees

#### GET /employees
Returns all the rows in table **EMPLOYEE** with the **COUNTRY_CODE** key value pair replaced by the **COUNTRY** key which retrieves back the country name using the <https://restcountries.eu/rest/v2/alpha?codes={code1};{code1};{code1}> API endpoint from <https://restcountries.eu>.  
This function is present in all queries that involve retrieving back **EMPLOYEE** information.

#### GET /employees/active
The document specified "Return all employees who DO NOT have a leave_date set or have a leave_date set in the
**past**".  
Returns all rows where the (**LEAVE_DATE** == **None**) **OR** (**LEAVE_DATE** < datetime.date.today())  
There is *one small issue with the logic*.  
If leave date is set as before the current date of today that would mean that the employee has already left the company.
This query will thus retrieve all current employees and all employees who have already left the company, leaving absent the employees that are yet to leave the company.  
The logic to return only the current employees would be (**LEAVE_DATE** == **None**) **OR** (**LEAVE_DATE** > datetime.date.today()) thus only employees still in the company will be retrieved. 
Should no employees be current a **404 error** message will be returned.  

#### GET /employees?department_name=[department_name]
Returns all employees given the department name.
This requires a left join between the **EMPLOYEE**, **JOB_TITLE** and **DEPARTMENT** tables.

## Observations
### restcountries.eu
During development, while attempting to call the **restcountries** recommended API endpoint for country names I noticed that while it being given **irl** it would not return Ireland. This was due to the **COUNTRY_CODE** value being correct for alpha encoding but not being the official supported country prefix which is ie. Thus I was forced to get creative and instead query by alpha encodings which were able to cover all edge cases.  
#
Thus the endpoint <https://restcountries.eu/rest/v2/name/irl?fullText=true> will not return the name Ireland but if using the alternative endpoint <https://restcountries.eu/rest/v2/alpha?codes=irl;irl;irl> the name of the country can be extracted from the returned json.  
#
While this method does work, it is not the most optimal solution.  
Everytime the **employees** endpoint is called, it has to make a call to the **restcountries** API. Thus the time delay is significantly increased and should the number of rows increase into the thousands it will adversely effect this endpoint.  
A better solution would be to perhaps have a table which can have the **COUNTRY_NAMES** as a variable. Therefore to get country names we would only have to do a basic join rather than query another API.
#
### reqparse
I 
note about regparse deprecation <https://flask-restful.readthedocs.io/en/latest/reqparse.html>

### Basic Authentication
The HTTPBasicAuth package is used for generating a login popup asking for username and password.  
The username and password will then be compared to the stored information.  
Due to not having a USER table with login information, the pasword and username are fetched from the ones given in the db_cred.py file.
