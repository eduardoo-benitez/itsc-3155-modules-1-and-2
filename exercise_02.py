word = input("Enter a string: ")
suffix = input("Enter another string: ")

wordSuffix = word[-len(suffix):]

if(wordSuffix == suffix):
    print("True")
else:
    print("False")