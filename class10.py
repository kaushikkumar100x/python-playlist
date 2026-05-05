# 1. Print a string

# a = "kaushik kumar"
# print("you name is", a)

# 2. Take string input and print
# name = input("Enter your name :")
# print("Welcome to",name)

# 3. Find length of string
# a = input("Enter the string :")
# print("your string length is ",len(a),"your string is", a)


# 4. Convert to uppercase

# a = input("Enter the string :")
# print("your string is ",a.upper())

# 5. Convert to lowercase
# a = input("Enter the string :")
# print("your string is ", a.lower())

# 6. Capitalize string
# a = input("Enter the string :")
# print("your string is ", a.capitalize())


#7. Count occurrences

# a = input("Enter the string :")
# print("your string is ", a.count("k"))

# 8. Find index
# a = input("Enter the string :")
# print("your string is find",a.find("k"))

# 9. Replace word
# a = input("Enter the string :")
# print("your string is ", a.replace("a","A"))

#10. Startswith

# a = input("Enter the string :")

# print("your string is starts :", a.startswith("The"))

# 11. Endswith

# a = input("Enter the string :")
# print("your string is end :",a.endswith("."))


# 12. Strip spaces

# a = input("Enter the string :")
# print("your string is strip :",a.strip())


# 13. Split string

# a = input("Enter the string :")
# print("your string is split :",a.split())


# 14. Join list

# a = input("Enter the string :")
# print("your string is join :", "+".join(a.split()))

# 15. Reverse string
# a = input("Enter the string :")
# print("your string is reverse :",a[::-1])


# 16. Palindrome check

# a = input("Enter the string :")
# if a == a[::-1]:
#     print("your string is palindrome")
# else:
#     print("your string is not palindrome")
# 17. Substring
# a = input("Enter the string :")
# print("your string is substring :",a[0:4])

# 18. Check numeric
# a = input("Enter the string :")
# print("your string is numeric",a.isnumeric()) 

# 19. Check alphabetic
# a = input("Enter the string :")
# print("your string is alphabetic",a.isalpha())

# 19. formatoing string


name = input("Enter your name :")
age = int(input("Enter your age :"))
branch = input("Enter your branch :")
marks = float(input("Enter your marks :"))

print("my name is {}. my age is {}. my branch is {}.my marks is {}".format(name,age,branch,marks))
print(f"my name is {name}. my age is {age}. my branch is {branch}.my marks is {marks}")