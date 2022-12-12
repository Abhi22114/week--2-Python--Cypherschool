#defults parameters
first_name="Abhijeet"
last_name="Kumar"
age=23
def user_info(first_name,last_name,age):
    print(f"your first name is {first_name}")
    print(f"your last_name is {last_name}")
    print(f"your age is {age}")
user_info(first_name,last_name,age)

# note:- non-defaults aruguments cannot follow the defults arguments
#if you defult the all arguments then you have to just pass the value user_info()