def binaryToGray(n):
    if not (n):
        return 0
    a = n % 10
    b = int(n / 10) % 10
    if (a and not (b)) or (not (a) and b):
        return (1 + 10 * binaryToGray(int(n / 10)))
    return (10 * binaryToGray(int(n / 10)))
binaryNumber = int(input("Enter the binary number:"))
print(binaryToGray(binaryNumber), end='')



#Lucciffer
