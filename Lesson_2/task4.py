InputNumber = int(input("Enter the factorial number: "))
variable = 1

if InputNumber == 0:
   print ("The factorial of the number is 0")
else:   
  while InputNumber > 0:
   factorial = InputNumber * variable
   InputNumber = InputNumber - 1
   variable = factorial

  print ("Factorial of the number: ", factorial)


