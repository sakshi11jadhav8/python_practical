
# Determine whether given number is harshad number or not...!!

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

if sum % 12 == 0:
    print(num,"given number is harshad number ")
else:
    print(num,"given number is not a harshad number ")
