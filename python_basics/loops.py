# print TC_1
# TC_2
# TC_3
# TC_4
# TC_5

for i in range(1,6):
    print("TC_",i)

#Print even numbers from 2 to 10 using for

for i in range(2,10,2):
    print(i)

#Use while to print:
#Retry 1
#Retry 2
#Retry 3
i=1
while i<=3:
    print("Retry",i)
    i+=1

# Loop from 1 to 5
#Skip 3
#Stop completely at 4

for i in range(1,6):
    if i==3:
        print("Skipping 3")
        continue
    if i==4:
        print("stopping the loop")
        break
# Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#Print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#Print odd numbers between 1 and 10
for i in range(1,10,2):
    print(i)

#Loop from 1 to 10
#Skip all even numbers
#Print only odd numbers

for i in range(1,10):
    if i%2==0:
        print("skipping even numbers")
        continue
    else:
        print("printing odd numbers")
        print(i)

#Loop from 1 to 10
#Stop the loop when number becomes 6
for i in range(1,10):
     print(i)
     if i==6:
         print("stopping at 6")
         break

#Loop from 1 to 10 ,
# Skip 4
# Skip 7
# Print all other numbers

for i in range(1,10):
    if i==4:
        print("skipping 4")
        continue
    if i==7:
        print("skipping 7")
        continue
    print(i)
#Using while, print:
# Attempt 1
# Attempt 2
# Attempt 3
# Attempt 4
# Attempt 5

i=1
while i<=5:
    print("Attempt", i)
    i+=1

# Using while, print numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1

# Write a while loop that runs forever,
# then fix it so it stops at 3
i=1
while i>=1:
    print(i)
    i+=1
    if i==3:
        print("stopping at 3")
        break
