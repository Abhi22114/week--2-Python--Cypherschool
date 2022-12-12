

#define a function thet take list of words as arguments and
#return  list with reverse of every elemenet in that list

#example
# ['abc,'tuv,'xvt']------>>>>>>['cba,'vut','tvx']
def reverse_element(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
words=["abc","tuv","xvt"]      
print(reverse_element(words)) 
