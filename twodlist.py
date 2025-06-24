twodlist= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
            ]
mylist = [1,2,3,4]
print(twodlist[0][1])
twodlist.append([17,18,19,20])
twodlist= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
            ]
print(twodlist)
#twodlist[0].append(10)
print(twodlist)
for row in twodlist: 
    for item in row: 
        print(item)
print("For i,j")
for i in range(len(twodlist)): 
    for j in range(len(twodlist[0])):

        print(twodlist[i][j])