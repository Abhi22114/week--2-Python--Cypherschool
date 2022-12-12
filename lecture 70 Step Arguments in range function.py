# we will discuss range function in step arguments

# for i in range (1,11,):  
    # for printing the numbers from 1 to 10 we can simply do this 
    # print(i)


#for print odd number b/w two given numbers using step arguments

for i in range(1,11,2):  #(here 2 will show step arguments and the reults will be printed be of 1 step distance  )
   print(i)

# for printing even numbers b/w two given numbers    


for i in range (0,15,2):            #------>>>>>>2 works as  3rd step arguments and will print the results as 1 step distance

    print(i)

#if you are ask to print the number from 10 to 1 (backward)    

for i in range (10,0,-1):  #-1 
    print(i)

# if you are ask to print the output from 1 to -11
for i in range (1,-11,-1) :    #3rd step arguments must not be zero
    print(i)    