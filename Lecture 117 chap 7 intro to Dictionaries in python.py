#DICTIONARIES
#Q-why we use dictionaries?
#ans-because of limitations of list,list are not enough to represent
#real data

#example
# user=['abc',17,['orange','kiwi no '],['you','fairy tale']]
 
# Q--what are dictionaries?
#as- unorded collection of data in key:value pair.

#how to create dictionaries?
# in dictiopnaries items are store under curly brackets{}
user={'name': 'abhijeet','age': 18}
print(user)
print(type(user))

#2nd method to create dictionaries
user1=dict(name="abhijeet",age=18)   #dict method 
print(user1)


#How to access data in Dictionaries
print(user['name'])    

#NOTE-in dictionaries the is no indexing because it is the collection of unordered items 

# what type of data can store in dictionaries  
# we can store anything in dictionaries as numbers ,strings,list,dictionary
user_info={
    'name':'abhijeet',
    'age':18,
    "fav dish":['chicken chilly','chicken tandorri'],

}
print(type(user_info))