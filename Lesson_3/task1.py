
def operationAddition (NumberFirst, NumberSecond):
    return NumberFirst + NumberSecond

def operationSubtraction (NumberFirst, NumberSecond):
    return NumberFirst - NumberSecond

def operationMultiplication (NumberFirst, NumberSecond):
    return NumberFirst * NumberSecond

def operationDivision (NumberFirst, NumberSecond):
    return NumberFirst / NumberSecond

def operationSquareNum(NumberFirst):
    return NumberFirst * NumberFirst

def main():
    print("You can do operation: Addition(+), Subtraction(-), Multiplication(*), Division(/)")
    operation = input("Choise the operation:")
    NumberFirst = int(input("Enter first number: "))
    NumberSecond = int(input("Enter second number: "))
    choice_operation(NumberFirst,NumberSecond,operation) 

def choice_operation(NumberFirst,NumberSecond,operation):
    match operation:
        case "+":
            print("Result operation: " + str(operationAddition(NumberFirst, NumberSecond)))
        case "-":
            print("Result operation: " + str(operationSubtraction(NumberFirst, NumberSecond)))
        case "*":
            print("Result operation: " + str(operationMultiplication(NumberFirst, NumberSecond)))
        case "/":
            print("Result operation: " + str(operationDivision(NumberFirst, NumberSecond))) 
        case _:
            print("Іnvalid value. Try again...")
            main()

main()