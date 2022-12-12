

def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>c and a>b:
        return a
    elif b>a and b>c:
        return b
    else :
        return c

def new_greatest(a,b,c):
    # bigger  = greater(a,b)
    return greater(greater(a,b),c)     
print(new_greatest(100,3,2))






#kiss ->>>>keep it simple stupid
#function inside a function
#greater(a,b)---->>>> a or b
#greater(a or b,c)--->>>greatest