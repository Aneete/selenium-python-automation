# Check if the word "success" exists in a string


login_status = "login successful"
if "successful" in login_status:
    print("Login successful")

# Convert "LOGIN FAILED" to lowercase
string1 = "LOGIN FAILED"
print(string1.lower())

# Remove extra spaces from " welcome "

msg = " welcome "
print(msg.strip())

# Split "one,two,three" into a list

num = "one,two,three"
items = (num.split(","))
print(items)

# Create a dynamic message using f-string with username & status

username = "admin"
statuscode = "success"
print(f"the login status of {username} is {statuscode}")


