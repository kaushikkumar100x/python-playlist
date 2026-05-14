# 1. Create and print a list
# a = []
# print(type(a))

# 2. Access first and last element

# a = [1,2,3,4,5,6]
# print("first element",a[0])
# print("Last element",a[5])

# 3. Add element using append()

# a = ["kaushik kumar","Shivam"]
# a.append("farhan")
# print(a)

# 4. Insert element at position

# a = ["kaushik kumar","shivam","Ram","dimpal"]
# a.insert(1,"farhan")
# print(a)

# 5. Remove element
# a = ["kaushik kumar","shivam","Ram","dimpal"]
# a.remove("shivam")
# print(a)

# 6. Pop last element
# a = ["kaushik kumar","shivam","Ram","dimpal"]
# a.pop()
# print(a)

# 7. Length of list
# a = ["kaushik kumar","shivam","Ram","dimpal"]
# print(len(a))

# 8. Sort a list

# a = [5,4,7,8,5,6,1,2]
# a.sort()
# print(a)

# 9. Reverse a list
# a = [5,4,7,8,5,6,1,2]
# a.reverse()
# print(a)

# 10. Maximum element
# a = [5,4,7,8,5,6,1,2]
# print(max(a))
# print(min(a))

# 12. Sum of list elements

# a = [2,2,2]
# print(sum(a))

# 13. Search element
# a = [5,4,7,8,5,6,1,2]
# if 8 in a:
#     print("Involved")
# else:
#     print("not involved")

# 14. Count occurrences

# a = [4,4,5,5,8,4,5,4,4,]
# print(a.count(4))

# 15 copy list
# a = [4,4,5,5,8,4,5,4,4,]
# b = a.copy()
# print(b)


# 16 clear list
# a = [4,4,5,5,8,4,5,4,4,]

# a.clear()
# print(a)


# 17. Concatenate lists

# a = [1,2,3]
# b = ["kaushik","codelife100x","shivam"]
# print(a+b)

# 18. Traverse list
# b = ["kaushik","codelife100x","shivam"]
# for i in b:
#     print(i)
  
  
#   19. User input list

# a = []

# b = input("Enter the list :")
# a.append(b)
# print(a)


# a = []
# for i in range(3):
#   b = input("Enter the list :")
#   a.append(b)
# print(a)

# 20. Find even numbers

a = []

b = int(input("Enter the list :"))
a.append(b)
for i in a:
  if i%2 ==0:
    print("Even number :",i)
  else:
    print("Odd number :",i)