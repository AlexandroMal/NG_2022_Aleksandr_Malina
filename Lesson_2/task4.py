InputNumber = int(input("Enter the factorial number: "))
multiplier = 1

if InputNumber == 0:
   print ("The factorial of the number is 0")
else:   
  while InputNumber > 0:
   factorial = InputNumber * multiplier
   InputNumber = InputNumber - 1
   multiplier = factorial

  print ("Factorial of the number: ", factorial)


