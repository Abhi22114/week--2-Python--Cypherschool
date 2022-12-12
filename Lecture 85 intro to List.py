#List = An orderded collection of items ,can store any datatypes ,int,float,string
#we can mix numbers ,string,in list
#none and 0 have differnt  valve 
#list is assingn by[] 

numbers=[1,2,3,4]
print(numbers)
print(numbers[0])
#we can also use slicing in list ,list slicing is same as string 

word=["apples","oranges","bananas"]
print(word)
print(word[-1])

mixed=[1,2,3,4,"apples","dog",2.3,None]
# print(mixed)

# print(mixed[5])

# mixed[1]='abhijeet','kumar' #if we want to replace a elements in the list (at 2nd postion)

print(mixed)

#if we have to break
mixed[1:]=["abhijeet","kumar"]
print(mixed)
 #all item excluding 1 will be break 