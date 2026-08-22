#Problem #2
#Descending numbers hehe

n = int(input("Enter input: "))

i = n
while i > 0:
    j = i
    line = ""
    while j > 0:
        line += str(j)
        j -= 1
    print(line)
    i -= 1
