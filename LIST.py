#Read 5 numbers, put them in a list, and print the list
#Change the 2nd element of the list (index 1)
#Append 600 to the end
#Insert 300 at the 3rd position (index 2)
#Remove the 2nd to the last element (index -2)
#Print the updated list
numbers = []
for i in range(5):
    num = int(input(f"Enter integer no. {i + 1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

new_value = int(input("\nEnter a new value for the 2nd integer: "))
numbers[1] = new_value
numbers.append(600)
numbers.insert(2, 300)
del numbers[-2]

print("\nUpdated List:", numbers)
