user_info={
    'name':'abhijeet',
    'age':18,
    "fav dish":['chicken chilly','chicken tandorri'],

}
print(type(user_info))

#add data

user_info['fav song']=['koi mil gaya','barish ban jana']
print(user_info)

#Remove
#pop method 
# popped_item=user_info.pop('fav dish')
# print(f"poped item is{popped_item}")
# print(user_info)

# pop item method (randomly koi item delete karne ke liye use karte hai)
popped_item=user_info.popitem()
print(user_info)
print(popped_item)