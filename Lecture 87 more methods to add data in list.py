
#we can add arguments  at any position in a given list  using insert  method 
#how to join (concatenate)  two list
#extend method 
#diffrence b/w append and extend method 

fruits1=['aaples','oranges','grapes','sugercane']
# suppose if you want to insert berry at 1 position
#fruits1.insert(1,'beery')
#print(fruits1)
#fruits1.insert(3,'carrot')
#print(fruits1)

fruits2=['berry','chiku','stwaberry']
#if you want to add these to list of fruits,you can add as:
#fruits3=fruits1 + fruits2
#print(fruits3)

#how to concatenate list into a list (this can be done using append method)

fruits1.extend(fruits2)       #extend method extend elements in a list
print(fruits1)
#print(fruits2)


fruits1.append(fruits2)  # with append we can concatenate list into a list
print(fruits1)