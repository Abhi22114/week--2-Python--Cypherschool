# in keywords and iterations in dictionaries




user_info={
    'name':'abhijeet',
    'age':18,
    "fav dish":['chicken chilly','chicken tandorri'],

}
print(type(user_info))

# check if key exist in the dictionaries
# if 'name' in user_info:
    # print('present')
# else:
    # print("not present")    

 # check if valve exist or not  ---->>values method 
user_info={
    'name':'abhijeet',
    'age':18,
    "fav dish":['chicken chilly','chicken tandorri'],

}
if 'abhijeet' in user_info.values():
    print('present')
else:
    print('not present') 

#loops in dictionaries
# for i in user_info:     #(this will print all the keys )
    # print(i)          
# user_info_valuses=user_info.values 
# print(user_info_valuses)   
# print(type(user_info_valuses))

# items method 
user_items=user_info.items()
print(user_items)
print(type(user_items))

for i,j in user_info.items():
    print(f"key is {i} and value is {j}")
