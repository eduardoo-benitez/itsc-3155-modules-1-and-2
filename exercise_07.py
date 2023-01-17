
list = []
flag = True

while flag:
    inp = input("Enter a number or QUIT to quit: ")
    if inp == "QUIT":
        flag = False
    else: 
        list.append(int(inp))
    
print("All nums: " + str(list))

evenList = []

for n in list:
    if n % 2 == 0:
        evenList.append(n)

print("Even nums: " + str(evenList))
