
# To check whether the number is prime or not...!!


num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if (num%i==0):
        prime = false
        break
if prime:
        print("This number is prime")
else:
        print("This numberr is not prime")
    
