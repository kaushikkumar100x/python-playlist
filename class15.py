# 2. What is a for loop?
# for i in range(1,11):
#     print(i)

# 3. What is a while loop?

# i = 1
# while(i<=10):
#     print(i)
#     i+=1

# 6. What is nested loop?

# for i in range(1,5): #row
#     print(i,"\n")
#     for j in range(0,2):#col
#         print(j,"\n",end="")
#         for z in range(0,1):
#             print(z , "\n")
        
    
# 7. What is break statement?

# for i in range(1,6):
#     if i ==4:
#         break
#     print(i)
    
    
  # 8. What is continue statement?  
    
# for i in range(1,6):
#     if i ==4:
#         continue
#     print(i)
    
    
    
# for i in range(1,6):
#     if i ==4:
#         print(i)
#         pass
   
   
#    9. What is infinite loop?


# while True:
#     print("kaushik kumar")


# 11. Print numbers from 1 to 10
# i = 1
# while(i<=10):
#     print(i)
#     i+=1


# 12. Print even numbers from 1 to 20


# i = 0
# while(i<=20):
#     if i%2 ==0:
#         print(i,"Even number")
#     i+=1
    
    
    # 13. Sum of first 10 natural numbers
    
# sum = 0
# for i in range(1,11):
#     print(sum)
#     sum +=i


# a = int(input("Enter the number :"))
# for i in range(1,11):
#     print(a*i)


# 15. Reverse counting


# for i in range(10,0,-1):
#     print(i)

# 16. Count digits \\homework

# 17. Factorial

# a = 5
# fact = 1
# for i in range(1,a+1):
#     fact *= i
#     print(fact)
    
    # 18. Prime number
# num = int(input("Enter the number :"))
# # flag = True
# for i in range(2,num):
#     if num % i == 0:
#         # flag = False
#         break
# print('Prime' if False else 'Not Prime')
    
    
    
    # 19. Star pattern \\homework
    
    # 20. Fibonacci series



a = 0
b = 1
for i in range(5):
    print(a)
    a = b
    b = a+b
    
    
    