#Practise for loop
#ask the user  a number like 2345
#calculate sum of digits ------>>>> 2+3+4+5


#Logic
#num ="2345"
#int(num[0])---->2
#int(num[1])-->>>3
#int(num[2])--->>4
#int(num[3])--->>5


# total=0
# num=input("enter the number : ")
# for i in range (0,len(num)):
    # total+=int(num[i])
    # print(i)                # here using print(i) will give out the position of number 
# print(total)    


#ex:-
total=0
num=123456789
for i in range (0,9):
    total+=i
    print(i)
print(total)    
