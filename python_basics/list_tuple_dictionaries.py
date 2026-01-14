#Create a list of 5 numbers and print only even numbers

numbers = [1,2,3,4,5]
for n in numbers:
    if n%2 ==0:
        print(n)

#Create a tuple of browser names and print each one

browsers = ("Chrome","Firefox","Edge","Safari")
for browser in browsers:
    print(browser)

# Create a dictionary for a user (username, role, active)

user = {"username" : "admin","role":"superadmin","active":True}
print(user["username"],user["role"],user["active"])

# Create a list of dictionaries for 3 users and loop through them
users =[
    {"username" : "admin"},
{"username" : "agent"},
{"username" : "supervisor"}
]
for user in users:
    print(user["username"])

# Write a function that accepts a dictionary and prints login info
login_info = {"username": "admin", "password": "Pass123#"}
def login_information(info):
    print("username:", info["username"])
    print("password:",info["password"])

login_information(login_info)
