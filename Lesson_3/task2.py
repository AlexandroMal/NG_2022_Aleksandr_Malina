
def out_information():
    print ("Yon can do this operation:", "1:Sorting string;" , "2:Calculate the number of elements;" ,\
    "3:Derive only vowel and consonant letters;" , "4:Outputting words from the end of a string;",\
    "5:Output the word by number;", "6:Enter the string again;" ,"7:Quit the program.", sep="\n")

def input_numbers():
    String = input("Enter the string: ")
    print(f'Your string: {String}')
    return String

def input_operation(operation):
    return input(operation)

def operation_sorting(string):
    string = string.split(" ") 
    string.sort()
    print(f'Sorted string: {string}')

def operation_replacement(string):
    string = string.split(" ") 
    string.reverse()
    print(string)

def numbers_elements(string):
    string = string.split(" ") 
    print("Elements og numbers: ", len(string))

def letter_count(String):
    a = []
    print("You wanna vowel or consonant letters?","1 - Vowel letters;","2 - Consonant letter.", sep="\n")
    choice = input("Enter: ")

    if choice == "1":
        for letter in String:
            if letter in "aeiou":
                a.append(letter)
        print(a)

    if choice == "2":
        for letter in String:
            if letter in 'bcdfghjklmnpqrstvwxz':
                a.append(letter)
        print(a)
    
def find_elements(string):
    index = int(input("Enter number of element: "))
    string = string.split(" ") 
    print(f"Element number {index}: ", string[index-1])

def choice_menu():
    String = input_numbers()
    inputOperation = input_operation("Choice the operation: ")
    if inputOperation == "1":
        operation_sorting(String)
    if inputOperation == "2":
        numbers_elements(String)
    if inputOperation == "3":
        letter_count(String)
    if inputOperation == "4":
        operation_replacement(String)
    if inputOperation == "5":
        find_elements(String)
    if inputOperation == "6":
        choice_menu()
    if inputOperation == "7":
        exit
    
def main():
    out_information()
    choice_menu()
    again = input("If you wanna try again enter -Yes-, or program to close: ")
    if again == "Yes" or "yes":
        main()
    else:
        exit

main()
