# 1. Check Even or Odd
# a = int(input("Enter your number : "))
# if (a%2 == 0):
#     print("Your number is even :", a)
# else:
#     print("Your number is odd :", a)


# 2. Positive or Negative
# a = int(input("Enter the number :"))
# if(a>=0 ):
#     print("Your number is positive :",a)
# else:
#     print("Your number is negative :",a)

# 3. Voting Eligibility

# a = int(input("Enter your age :"))
# if(a>=18):
#     print("You are eligible for voting :",a)
# else:
#     print("You are not eligible for voting :",a)


# 4. Greater Number

# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# if(a>b):
#     print("The first number is greater :",a)
# elif(a<b):
#     print("The second number is greater :",b)
# elif(a==b):
#     print("Both numbers are equal :",a,b)
# else:
#     print("Invalid input :",a,b)


# 5. Divisible by 5

# a = int(input("Enter the number ;"))
# if(a%5==0):
#     print("true",a)
# else:
#     print("false",a)

# 6. Largest of Three
# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# c = int(input("Enter the third number :"))
# if(a>b and a>c):
#     print("The first number is largest :",a)
# elif(b>a and b>c):
#     print("The second number is largest :",b)
# elif(c>a and c>b):
#     print("The third number is largest :",c)
# elif(a==b and a>c):
#     print("The first and second numbers are largest :",a,b)
# elif(a==c and a>b):
#     print("The first and third numbers are largest :",a,c)
# elif(b==c and b>a):
#     print("The second and third numbers are largest :",b,c)
# elif(a==b and a==c):
#     print("All three numbers are equal :",a,b,c)
# else:
#     print("invalid number:")

# 7. Leap Year
# a =  int(input("Enter the year :"))
# if(a%4==0 and a%100!=0)or(a%400 ==0):
#     print("The year is a leap year :",a)
# else:
#     print("The year is not a leap year :",a)

# 8. Grade Calculator  homework

# 9. Zero Check

# a = int(input("Enter the number :"))
# if(a ==0):
#     print("The number is zero :",a)
# else:
#     print("The number is not zero :",a)

# 10. Vowel or Consonant


# a = input("Enter the character :")
# if a in"aeiouAEIOU":
#     print("The character is a vowel :",a)
# else:
#     print("The character is a consonant :",a)


# 11. Smallest Number homework

# 12. Pass or Fail
# a = int(input("Enter the marks :"))
# if a<33:
#     print("You are fail :",a)
# else:
#     print("You are pass :",a)

# 15. Temperature Check
# temp = int(input("Enter the temperature :"))
# if temp>30:
#     print("It's a hot day :",temp)
# else:
#     print("It's a cold day :",temp)

#14. Login System

# password = input("Enter the password :")
# if password == "shivam@123":
#     print("Login successful")
# else:
#     print("Login failed")


# 16. Simple Calculator homework

# 17. Range Check homework
# 18. Alphabet Check homework
# 19. Absolute Value homework

# 20. Username and Password

# us = input("Enter the username :")
# pw = input("Enter the password :")
# if us == "codelife100x" and pw == "shivam@123":
#     print("Login successful")
# else:
#     print("Login failed")



#self practice 
hin = int(input("Enter the marks of Hindi :"))
eng = int(input("Enter the marks of English :"))
mat = int(input("Enter the marks of Mathematics :")) 
sci = int(input("Enter the marks of Science :"))
sst = int(input("Enter the marks of Social Science :"))

a = hin + eng + mat + sci + sst

print("your total marks is :",a)

b = a/5
if(b>=90):
    print("your grade is A",b)
elif(b>=75):
    print("your grade is B",b)
elif b>=50:
    print("your grade is C",b)
elif (b>=33):
    print("your grade is D",b)
else:
    print("your grade is F and so you failed",b) 