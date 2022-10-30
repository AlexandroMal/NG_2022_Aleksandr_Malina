#Entering data, converting it from str to int, and sorting numbers
number = input("Enter numbers: ")
lst = number.split(",") 
lst = [int(x) for x in lst]
lst.sort()

#calculate sum of numbers in list in range (1:-1)
sum = 0
for i in lst[1:-1]:
    sum=sum+int(i)

#Display sum, max and min number from the list
print("Sorted list: " + str(lst))
print("Max number in the list: " + str(lst[0]), "Min number in the list: " + str(lst[-1]),"Sum of other numbers: " + str(sum), sep="\n")
