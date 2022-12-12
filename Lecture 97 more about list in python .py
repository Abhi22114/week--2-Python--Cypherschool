# generate lists with the help of range function
# something more about pop method 
# index method
# pass list method 

# -1) generate lists with the help of range function
numbers=list(range(1,11))
print(numbers) #this how we can create a list using range function

# 2) something more about pop method 
numbers1=list(range(1,11))
popped_item=numbers1.pop
print(numbers1)

# 3) index method

numbers2=[1,2,3,4,5,67]
# print(numbers2[0])

print(numbers2.index(1))
# print(numbers2.index(1,6))


# 4) pass list method 

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)

    return negative
print(negative_list(numbers))



