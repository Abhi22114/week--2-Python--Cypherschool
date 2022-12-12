#we wiil define a function for printing the greatest of the three arguments
a=45
b=56
c=50

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(a,b,c))



