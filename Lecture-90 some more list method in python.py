

#count method   
# sort method 
#sorted function
# reverse
# copy
# clear5
fruits=['banana','apple','grapes','orange','kiwi','kiwi']
# print(fruits.count('kiwi'))  # (fruits.count)--->> gives the output of how ,much time kiwi comes in the list

# by sort method we can arrange the item in the list alphabetly
fruits.sort()    
print(fruits)

numbers=[2,8,9,4,1,34,98,3,6]
numbers.sort()
print(numbers)

# numbers1=[1,5,6,2,356,23,21]
 
#print(sorted(numbers1))
numbers2=[1,45,67,9,0,2,1,45,23]
numbers2.clear()       #Clear method will empty our list
print(numbers2)

# copy method is used to make a copy of list or numbers
numbers3=[1,34,4,5,6,7]
numbers3_copy=numbers3.copy()
print(numbers3)