# Program to learn variables,type,id,reference

Name = "Aneete Rose"
Age = 25
Height = 5.4
is_testengineer = True

print("Name:", Name)
print("Age:",Age)
print("Height",Height)
print("Is_testengineer:",is_testengineer)

# Type of each variable
print(type(Name))
print(type(Age))
print(type(Height))
print(type(is_testengineer))

# id of each variable(memory address)
print("id of name:",id(Name))
print("id of age:",id(Age))
print("id of height:",id(Height))
print("id of is_testengineer:",id(is_testengineer))

# reference variables - pointing to same object
a= 100
b=200
c= b
print(a)
print(b)
print(c)
print("id of a",id(a))
print("id of b",id(b))
print("id of c",id(c))

x="10"
print(type(x))

#Fix this code:print("Attempt " + 3)

print("attempt",3)

# converting"15.5" to float and print
x="15.5"
print(type(x))
y=float(x)
print(y)

#Take user input for status code and compare with 200
a = int(input("Enter the status code"))
print(a)
print(type(a))
print(a==200)








