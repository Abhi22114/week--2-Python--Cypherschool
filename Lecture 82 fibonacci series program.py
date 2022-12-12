#FABONACCI SERIES
#0 1 1 2 3 5 8 13 21 34 (sum of last two number)

#for i in range(1,11):  
#    print(i) #print the output in different line:-

#for i in range(1,12):
 #   print(i,end=" ")
   # print(i,end=",")    # this will print the results in same line comma separated 
   # print(i, end = "\n")  #back slash n diffrent line me value print hoga


def fibonacci_seq(n):
    a=0  #first number
    b=1  #2nd mumber
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b) #a,b,0,1   
    else:
        print(a,b ,end =" ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b ,end=" ")
# fibonacci_seq(20) 
fibonacci_seq(29)           




