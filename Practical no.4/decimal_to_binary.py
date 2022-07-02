

# python program to convert the decimal number to binary number..!!

def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num//2)
    print(num%2,end=" ")

number = int(input("Enter a decimal number : "))

decimalToBinary(number)
