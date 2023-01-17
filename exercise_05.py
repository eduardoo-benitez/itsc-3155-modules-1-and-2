
i = 0
listOne = []

while (i < 5):
    inp = input("Enter a number for the first list: ")
    listOne.append(inp)
    i += 1

listTwo = []

while(i <= 5 and i > 0):
    inp = input("Enter a number for the second list: ")
    listTwo.append(inp)
    i -= 1

print("First list: " + str(listOne))
print("Second list: " + str(listTwo))

commonList = []

for num1 in listOne:
    for num2 in listTwo:
        if num1 == num2 and commonList.__contains__(num1) == False:
            commonList.append(num1)

print("Common list: " + str(commonList))