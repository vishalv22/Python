# 3. Check the type of Variable assigned using input() function.
a = input("Enter anything: ")
print(type(a))           # doesnot matter what we give input, type will be considered as string




# 4. Use Comparision Operator to find out whether a given variable is greater than 'b' or not.

print("Check if a is greater than b")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(a > b)



# 5. Write a python program to find an average of 4 numbers entered by the user.
print("Find Average of 2 numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Averagr number is: ", (a + b) / 2)



# Q6. Write a Python program to calculate the Square of a Number entered by the user.
print("To know the square of a number,")
a = int(input("Enter the number: "))
print("The square of the number", a,"is",a ** 2)