# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a)#output 3
print(a==b) # otput false

print(a == b)   # False checks for equality
print(a != b)   # True checks if it is not equal
print(a > b)    # False checks for greater than
print(a < b)    # True checks for less than
print(a >= b)   # False checks for greater than or equal to 
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #output true
8 != 8 #output false
4 <= 2 + 2 # output true

# Write 3 examples that result in True and 3 that result in False.
print(20> 25)
print(40>30)
print(15<10)
print(30<10) 
print(10> 5)
print(20<29)
# Create a simple grade-checking condition:
#make this program for all grading spectrums
#if the score is between 90-100 you got an a
#if the score is 80-89 you got a b
#if the score is 70-79 you got a c
#if the score is 60-69 you got a d
#else = fail
score = int(input("what is your score")) 
if score >= 60:
    print ("you did pass")
else :
    print("you didnt pass")
#password

# practice problem :if score >=90 and score <=100:
if score >90 and <= 90:
    print("you got an A")
elif score >=80 and score is <=89:
    print("You goit a B")
elif score >= 70 and score<= 79:
    print("you got a C")
elif score >=60 and<=69:
    print ("you got a D") 
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
password = input ("What is your password")
if len(password) >=8 and any(char.is digit())

