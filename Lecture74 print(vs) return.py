# return vs print

#suppose we have to add three (a,b,c)
#def add_three(a,b,c):
   # return a+b+c
#add_three(5,5,5)    # gives no output



def add_three(a,b,c):

    return a+b+c
print(add_three(5,5,5))  


def add_three(a,b,c):
    print(a+b+c)
add_three(9,45,100)


#we can both write print and return but return is good for function 


