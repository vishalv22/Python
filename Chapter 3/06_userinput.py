a = input("Enter the First Number: ")
b = input("Enter the Second Number: ")

print("The sum of the Both numbers is: ", a + b)

#it will combine the two strings and print it as a single string.
#But we want to add two numbers, not two strings.

#Correct method: 
c = int(input("Enter the first Number: "))          # int(), now it will take input from user as a Number. 
d = int(input("Enter the second Number: "))

print("The sum of both Numbers is: ", c + d)