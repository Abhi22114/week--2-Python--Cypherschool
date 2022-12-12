#common elements finder function
#define a function which take 2 lists as input and return a list
#which contains common elements of both lists

#example
#input-->>>[1,2,5,8],[1,2,7,6]
#output--->>>[1,2]

def common_finder(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
l1=[1,2,5,8]
l2=[1,2,6,7]    
print(common_finder(l1,l2))