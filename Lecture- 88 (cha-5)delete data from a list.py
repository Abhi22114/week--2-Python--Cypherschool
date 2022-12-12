 #Common method to delete data from list

#this can be done through using pop method 

fruits=['orange','berry','pear','kiwi']
fruits.pop(1)    #here beery is at 1 position ,so beery will be delete 
print(fruits)


#we can also use del method
del fruits[0 and 1]
print(fruits)     #item at 0 and 1st postion(orange and beery will be deletd)

#remove method (this usually used when postion of item to be removed is not known )

fruits1=['apples','banana','kiwi','orange','apples']
fruits1.remove('apples')  #one apples from the list will be removed 
print(fruits1)