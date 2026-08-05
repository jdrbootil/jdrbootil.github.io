#Problem #1
#Accept 10 Integers
#Print the positive and negative numbers separately
#Print thesum of the  positive numbers and the average of thenegative numbers

nums = [int(input(f"Enter an integer {i+1}: ")) for i in range(10)]

positives = [n for n in nums if n > 0]
negatives = [n for n in nums if n < 0]

print("Positive numbers:", *positives)
print("Negative numbers:", *negatives)
print("Sum of positive integers:", sum(positives))

if negatives:
    print("Average of negative numbers:", sum(negatives) / len(negatives))
else:
    print("Average of negative numbers: N/A")
