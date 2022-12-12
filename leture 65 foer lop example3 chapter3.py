# parctise for loop
# ask the user and count each character(how much times the given character come in the given name )
# "Abhijeet kumar"

#then A:2
#b:1
#h:1
#i:1
#j:1
#e:2
#t:1
#k:1
#u:1
#m:1
#r:1
name="abhijeet kumar"  #name=("enter your name : ")
temp= ""
for i in range(len(name)):
    if name [i] not in temp:
        print(f"{name[i]}: {name.count(name [i])}")
        temp+= name[i]
        

name="ramayana ravan ram raja rishabh rishika "
temp=""
for i in range (len(name)):
    if name [i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}") 
        temp+=name[i]       