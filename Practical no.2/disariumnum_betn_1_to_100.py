
# To print the Disarium Number between 1 to 100...!!

def calculateLength(n):
    length = 0
    while(n != 0):
        length = length + 1
        n = n // 10
    return length

def sumOfDigits(num):
    rem = sum = 0
    len = calculateLength(num)
    

    while(num>0):
        rem = num % 10
        sum = sum + int(rem**len)
        num = num // 10
        len = len - 1
    return sum

result = 0

print("Disarium number between 1 to 100 are ")

for i in range(1,101):
      result = sumOfDigits(i)

      
    if(result == i):
      print(i)


