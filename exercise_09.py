
count = 0
list = []

while count < 5:
    list.append(input("Enter a word: "))
    count += 1

print("Words: " + str(list))

sentance = ""

for w in list:
    sentance += w + " "

print("One string: " + sentance)
