Number = int(input("Enter the number: "))
Number_2 = 1

if Number == 0:
   print ("The factorial of the number is 0")
else:   
  while Number > 0:
   factorial = Number * Number_2
   Number = Number - 1
   Number_2 = factorial

  print ("Factorial of the number:", factorial)


