#Problem #2
#Printing the fibonacci series of an input number
num = int(input("Enter a number of your choice: "))
n1, n2 = 0, 1
sum = 0
if num<=0:
    print("That's too low, enter a number greater than 0.")
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
