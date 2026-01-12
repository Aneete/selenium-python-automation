x = 5

if x > 3:
    print("A")
elif x > 10:
    print("B")
else:
    print("C")

# to enter status code and check condition
status_code = int(input("Enter the status code:"))
if status_code ==200:
    print("PASS")
elif status_code == 400 or status_code == 401:
    print("CLIENT ERROR")
else:
    print("SERVER ERROR")

# login validation using username, password, AND operator
username = "aneete"
password = "Pass123#"

if username == "aneete" and password == "Pass123#":
    print("Login successful")
else:
    print("Login Failed")
