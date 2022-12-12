# break and continue keywords

#break keyword is used to break a loop /or end a loop 

#print numbers from 1-10

# for i in range(1,11):
    # print(i)

# if you ask to break the loop at i ==5

for i in range(1,11):
   if i==5:    #(i==5 means num,bner will be printed from 1 to 4)
       break
   print(i)

#  continue keyword            -----____----->>>(we can skip the things using continue statement)

#ask to print 1 to 10 but not 5
#1,2,3,4,5,,6,7,8,9,10

for i in range (1,15):
    if i==5:
        continue    #(continue statement  helps to jump the excution  and print the the excluding 5)
    print(i)


for i in range (100,120):
    if i==108:
        continue
    print(i)

