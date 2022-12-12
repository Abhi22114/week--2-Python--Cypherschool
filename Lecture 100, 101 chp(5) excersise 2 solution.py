 #define a function which will take list argument and this function
 #will return reversed list
 #example
 #[1,2,3,4]----->>>>[4,3,2,1]
 #['word','word2']------>>>>['word2','word1]
 #note you simply do this reverse method or [:::-1]
 #but do this with return and append method


# def reverse_list(l):
    #return l.reverse()    #--->>thsi will print none 

    # l.reverse()
    # return l
# numbers=[1,2,3,4]
# print(reverse_list(numbers))

# def reverse_list(l):
    # return l[::-1]    #slicing
# numbers=[1,2,3,4]    
# print(reverse_list(numbers))    

def reverse_list(l):
    r_list=[]
    for i in range(1,len(l)+1):
        pooped_item=l.pop()
        r_list.append(pooped_item)
    return r_list   
numbers=[1,2,3,4]
print(reverse_list(numbers))