len = int(input("Enter a number: "))
i = 1
list = []

while (i <= len):
    list.append(input("Enter number " + str(i) + ": "))
    i += 1

print("List: " + str(list))

avg = 0
for val in list:
    avg += int(val)

print(float(avg/len))
