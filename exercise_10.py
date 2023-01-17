inp = input("Enter a string: ")

list = []
newList = []

count = 0
totalCount = 0
for l in inp:
    newList.append(l)
    count += 1
    totalCount += 1
    if count == 3:
        list.append(newList)
        newList = []
        count = 0
    if totalCount == inp.__len__():
        list.append(newList)
        newList = []
    

print(list)