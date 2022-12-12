#split method 
# this method  coverts string to a list

user_info="Abhijeet 18 ".split()
print(user_info)


#user_info='Abhijeet,18 '.split(',')
#print(user_info)


name , age ="Abhijeet 18 ".split()
print(name,age)
print(name)
print(age)


# join method 

#with this method we convert list to string 

user_info=["Abhijeet ,18 "]
print(",".join(user_info))      
