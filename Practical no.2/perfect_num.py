
# Python program to check if a number is a perfect number or not ...!!

n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    if(n%i == 0):
        sum = sum + i
if(sum == n):
    print("The number is a perfect number..!! ")
else:
    print("The number is not a perfect number..!!")
