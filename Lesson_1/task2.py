print ("=======================================================================================================")
print ("You can do operation: Addition(+), Subtraction(-), Multiplication(*), Division(/), Square number(^)")
print ("=======================================================================================================")
operation = input ("Choose which operation to perform: ")

if operation == "^":
    value_a = int (input ("Enter the number: "))
    print ("==================================")
else:
    value_a = int (input ("Enter the first number: "))
    value_b = int (input ("Enter the second number: "))
    print ("==================================")
    print ("The result of the operation: ", end="")

if operation == "+":
    print (str(value_a + value_b))
elif operation == "-":
    print(str (value_a - value_b)) 
elif operation == "*":
    print(str (value_a * value_b))
elif operation == "/":
    print(str (value_a / value_b))
elif operation == "^":
    print(str (value_a * value_a))
else:
    print("You entered an incorrect operation")

