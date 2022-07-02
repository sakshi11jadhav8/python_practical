

# Python program to convert the binary number to decimal number..!!


def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is :", decimal)

binary = input("Enter a binary number :")
BinaryToDecimal(binary)
