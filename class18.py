# a = []
# b =[1,505,"kaushik kumar"]
# print(b,type(b))

# print(b[0])
# print(b[-1])
# name = ["kaushik kumar","Shivam pal","Farhan","Dimpal","Ram"]
# print(name[0:3])




# append , extend
# a = [1,2,3]
# b = [4,5,6]
# # a.append(b)
# a.extend(b)
# print(a)


# insert ,pop
# a = [1,2,3,4,5]
# a.insert(0,99)
# a.pop()

# print(a)


# remove and clear

# a = [20,25,50,55,65,60,90,95]
# a.remove(25)
# a.clear()
# print(a)

# reverse and short


# a = [20,25,50,55,65,60,90,95]
# a.reverse()
# print(a)

# a = [1,58,45,78,56,89,58,47,26]
# a.sort()
# b = a.copy()
# print(b)


# a = [[1,5,5,4],[2,8,5,7],[4,8,9],[5,3,4,5,6]]
# print(a[-1])
# print(a)

# a = [i*i for i in range(1,6)]
# print(a)

# b = [i for i in range(100) if i%2 ==0]
# print(b,"even")

a = [1,58,45,78,56,89,58,47,26]
a.append(4)
print(id(a))