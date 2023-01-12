string = input("Enter a string: ")
letters = {}

for elements in string.lower():
    if elements != " ":
        try:
            letters[elements] = letters[elements] + 1
        except:
            letters[elements] = 1

print("\nSorted by letter: ")
for keys, values in sorted(letters.items()):
    print((f"{keys}: {values}"))

print("\nSorted by number: ")
for keys, values in sorted(letters.items(), key=lambda value: value[1], reverse=True):
    print((f"{keys}: {values}"))



