names = []

for i in range(3):
    name = input("Enter a name: ")
    names.append(name)

print(sorted(names, key=str.lower))