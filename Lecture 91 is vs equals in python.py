#List comparison
#==,is
fruits1=['orange','berry','pear','kiwi']
fruits2=['orange','berry','pear','kiwi']
fruits3=['orange','berry','pear','apple','kiwi']
print(fruits1==fruits2)  #values are same
print(fruits1==fruits2==fruits3)       #print false
print(fruits1 is fruits2)   #this will give output as false because (is) keyword checks that object is at same place in the memory or not  
