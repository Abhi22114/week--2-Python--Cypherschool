# list vs string
# string are imutable in python ,we cannot change the particular sting
# list are mutable 
 
s="abhijeet"
# s.title
#print(s) #the out will be printed as same ,not show any changes 
t=s.title()  #but after assinging  string to another varriable  abhijeet is printed as Abhijeet 
print(t) 

l=['word1','word2','word3']
# l.append("word3")
print(l)   #we can add ,remove ,append,items in list  in python
l.pop()
print(l)