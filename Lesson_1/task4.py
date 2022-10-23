
from tokenize import Double
import math
print ("======================================")
print("Quadratic equation: ax^2 + bx + c = 0:")
print ("======================================")
number_a = float(input("Enter the number a: "))
number_b = float(input("Enter the number b: "))
number_c = float(input("Enter the number c: "))
print ("==================================")
   
discriminant = ((number_b*number_b) - 4 * number_a * number_c)

if discriminant > 0:
    print ("Discriminant= %.3f" % discriminant)
    print ("Roots of the equation:")
    x_1 = (- number_b + math.sqrt(discriminant)) / (2 * number_a)
    print("x1 = %.3f" % x_1)
    x_2 = (- number_b - math.sqrt(discriminant)) / (2 * number_a)
    print("x2 = %.3f" % x_2)

if discriminant == 0:
    print ("Discriminant= 0")
    x = (- number_b / (2 * number_a))
    print("x = %.3f" % x)

if discriminant < 0:
    print ("Discriminant = %.3f" % discriminant)
    print ("There are no roots of the equation")

   