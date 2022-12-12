def func(int1,int2):
    add=int1+int2
    multiply=int1*int2
    return add,multiply
int1=2
int2=5
print(func(int1,int2))  #this will give output in tuple

#if we have to print valve separately
add,multiply=func(int1,int2)
print(multiply)
print(add)