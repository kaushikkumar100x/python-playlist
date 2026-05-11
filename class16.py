#solid square pattern

# for Row in range(1,5):
#     for col in range(1,5):
#         print("* ",end=" ")
#     print()    

#soild rectangle pattern

# for r in range(1,4):
#     for c in range(1,7):
#         print("* ",end="")
#     print()

# solid tri

# for t in range(1,6):
#     for c in range(t):
#         print("* "  ,end="")
#     print()
  
  
  #inverted tri

# for t in range(6,0,-1):
#     for c in range(t):
#         print("* "  ,end="")
#     print()

# pyramid

# n =5
# for i in range(n):
#     # part1
#     print("  "*(n-i-1),end="")
#     #part2
#     print("* "*(2*i-1))

#inverted


# n = 5
# for  i  in range(n-2,-1,-1):  #n
#     #tri
#     print("  "*(n-i-1)+ "* " *(2*i+1))
    
   
    
    
    #dimand solid
# n = 5
# for i in range(n):
#     #first
#     print("  "*(n-1-i) +"* " *(2*i+1))
    
#     #second
# for j in range(n-2,-1,-1):
#     print("  "*(n-1-j) +"* " *(2*j+1))


#left triangle

# n = 5
# for i in range(1,n+1):
#     #print
#     print("  "*(n-i)+ "* "*(i))
    
    
    # intvert left triangle
    
# n = 5
# for i in range(n,-1,-1):
#     #print
#     print("  "*(n-i)+ "* "*(i))
    
    
   # half  daimaond
   
n = 5

#upper part
# for i in range(1,n+1):
#     print("* "*i + "  "*(2*(n-1)))
    
    
# #lower part
# for j in range(n-1,0,-1):
#         print("* "*j + "  "*(2*(n-1)))
   
   
# n = 5
# for i in range(n):
#     print("  " *(n-1-i)+ "* "*n)

#solid 
#left part


n = 5
# upper 
for i in range(1,n+1):
    print("* "*i, end="")
    print("  " *2*(n-i),end="") 
    
    print(" *"*i)
    # lower
for j in range(n-1,-1,-1):
    
        print("* "*j, end="")
        print("  " *2*(n-j),end="")

        print(" *"*j)
    
