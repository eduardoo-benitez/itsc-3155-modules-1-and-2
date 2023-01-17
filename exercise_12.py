inp = input("Enter a string: ")
result = ""

inp.strip()

for c in inp:
    if c.islower():
        result += c

for c in inp:
    if c.isupper():
        result += c

print(result)