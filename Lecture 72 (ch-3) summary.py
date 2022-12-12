#1if  statement

# name ="Abhijeet"  
# if name=="Abhijeet":
    # print("I am Abhijeet" )

# elif name=="Raja " :

    # print("I am Raja") 
# else:
    # print("I am not Abhijeet or Raja")     

#2 While loop ---------->>>>>>(if you have to excuted a single code again and again  use while loop )    

# if you have to print a number less than 10 ( 9 to 1)
i=0
while i < 10 :
    print(i)   #------>>>>>(the valve )
    print('hello world')
    i+= 1
# 
# i=1
# while i <=10:
    # print(i)
    # print("hello world")
    # i+=1

#3 For loop --->>>>>>


#If you have to print print numbers from (1 to 10)

# for i in range (1,11):
    # print(i)
for i in range (1,11,3):  #(result will be printed as 3 step distance)
    print(i)     

#4 break keywords ------>>>>(used to break a loop)

for i in range (1,11):
    #print(i)
    if i ==5:
        break  #(statement will break as i =5    only ,1,2,3,4 printed)
    print(i)



# 5 Continue keyword------->>>>

# for i in range(1,11):
    # if i==6:
        # continue  #continue and 6 will not be printed excepted all will be printed
    # print(i) 

#6 -->>for loop in string to print each characters on new line 

for i in "Abhijeet kumar":
    print(i)