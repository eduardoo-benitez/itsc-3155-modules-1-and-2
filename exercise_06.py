row = int(input("Enter a row num from 1 to 5: "))

col = int(input("Enter a col num from 1 to 5: "))

r = 1
while r <= 5:
    c = 1
    while c <= 5:
        if row == r and col == c:
            print (1, end = " ")
        else:  
            print(0, end = " ")
        c += 1
    print("")
    r += 1
