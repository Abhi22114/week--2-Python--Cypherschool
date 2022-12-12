#varrible scope
def func():
    x=7     #local varriables x has its scope in def func() only
    return x
print(func())
#def func2():
 #   print(x)  #this will not give a results 
#func(2)      


#lets consider a global varriables 
#global varriables has not definite scope 

y=5
def func1():
    global y
    y=6     #local varriables 
    return y
print(y)                     #it is difficult to maintain our code  if we use global varribles inside a function
print(func1())   
print(y)