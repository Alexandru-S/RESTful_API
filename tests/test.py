import requests

BASE = "http://127.0.0.1:5000/"

# /department
# response = requests.get(BASE + 'department')
# print(response.json())

# # /badges
# response = requests.get(BASE + 'badges')
# print(response.json())
#
# /job_titles
response = requests.get(BASE + 'job_titles')
print(response.json())

# /employees
response = requests.get(BASE + 'employees')
print(response.json())
