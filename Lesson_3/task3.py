def resultOperation(number,letters,string):
    if number < len(string):
        elements = string[number]
        try:
            letters[elements] = letters[elements] == 0
        except:
            letters[elements] = 1
        resultOperation(number + 1,letters,string)
    return letters

string = input("Enter string: ")
number = 0
letters = {}
print("Number of letters:\n",resultOperation(number,letters,string))
