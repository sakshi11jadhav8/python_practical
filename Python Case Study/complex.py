# Write a python program to perform the following operations on complex numbers by
# creating a class complex_numberber. Create two objects c1 and c2.
# a. Addition
# b. Subtraction
# c. Multiplication
# d. Check if two complex numbers are equal or not
# e. Check if c1>=c2
# f. Check if c1<=c2
# Perform these operations using operator overloading in python.

class complex_number:
    def __init__(self):
        self.real = 0
        self.imag = 0

    def assign(self, rl, img):
        self.real = rl
        self.imag = img

# a. Addition
    def __add__(self, obj):
        temp = complex_number()
        r = self.real + obj.real
        i = self.imag + obj.imag
        temp.assign(r, i)
        return temp

# b. Subtraction
    def __sub__(self, obj):
        temp = complex_number()
        r = self.real - obj.real
        i = self.imag - obj.imag
        temp.assign(r, i)
        return temp

# c. Multiplication
    def __mul__(self, obj):
        temp = complex_number()
        r = self.real*obj.real - self.imag*obj.imag
        i = self.real*obj.imag + self.imag*obj.real
        temp.assign(r, i)
        return temp

# d. Check if c1==c2
    def __eq__(self, obj):
        if self.real == obj.real and self.imag == obj.imag:
            return True
        else:
            return False


# e. Check if c1>=c2
    def __ge__(self, obj):
        self = (self.real**2+self.imag**2)**0.5
        obj = (obj.real**2+obj.imag**2)**0.5
        if self >= obj:
            return True
        else:
            return False


# f. Check if c1<=c2
    def __le__(self, obj):
        self = (self.real**2+self.imag**2)**0.5
        obj = (obj.real**2+obj.imag**2)**0.5
        if self <= obj:
            return True
        else:
            return False


    def __str__(self):
        return str(self.real)+' + '+str(self.imag)+'i'


c1 = complex_number()
c2 = complex_number()

c1.assign(4, 12)
c2.assign(2, 10)

print("c1 =", c1)
print("c2 =", c2)
print("")

print("Additon:\t", c1+c2)
print("Subtraction:\t", c1-c2)
print("Multiplication:\t", c1*c2)
print("")

print(c1, "==", c2,":", c1 == c2)
print(c1, ">=", c2,":", c1 >= c2)
print(c1, "<=", c2,":", c1<=c2)
