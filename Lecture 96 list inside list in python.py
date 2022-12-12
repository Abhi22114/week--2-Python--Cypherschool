# We acn store list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]

# 3items --->>>>3 list
# print(matrix[2])
# print(matrix[0])

for i in matrix:
    print(i) #this will print the value as different list 


for sublist in matrix:
    for i in sublist : #this will print the results as numbers on diiferent line
        print(i)

#Type function

print(type(matrix)) 