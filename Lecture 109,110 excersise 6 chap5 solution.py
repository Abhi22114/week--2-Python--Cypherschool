#function
#input-->>[1,2,3,[1,2],[3,4]]
#2 output(numbers of list in the list)

def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed=[1,2,3,[1,2],[3,4]]            
print(sublist_counter(mixed))