inputNumber = int(input("Input size: "))

for a in range(inputNumber, 0, -1):
    for b in range(a, 0, -1):
        print(b, end = " ")
    print("\r")