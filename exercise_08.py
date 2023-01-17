count = 1
list = []
noDupList = []

while count <= 10:
    inp = input("Enter number " + str(count) + ": ")

    if list.__contains__(inp) == False:
        noDupList.append(inp)

    list.append(inp)
    count += 1

print("Original list: " + str(list))
print("Nums that appear once: " + str(noDupList))

