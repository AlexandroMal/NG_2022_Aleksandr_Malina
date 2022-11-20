inputNumber = int(input("Input size: "))

for totalNumber in range(inputNumber, 0, -1):
    for numbers in range(totalNumber, 0, -1):
        print(numbers, end = " ")
    print("\r")