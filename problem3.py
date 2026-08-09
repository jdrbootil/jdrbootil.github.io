#Problem #3
#Print the factorial series
#And print the results

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i

    series_list = [str(x) for x in range(num, 0, -1)]
    series_str = "*".join(series_list)

    print(f"Factorial series: {series_str}")
    print(f"Results: {factorial}")
