
# Python program to find the three consecutive common numbers in the list..!!

a = [1, 1, 1, 64, 23, 64, 22, 22, 22]

size = len(a)

for i in range(size - 2):
    if a[i] == a[i+1] and a[i+1] == a[i+2]:
        print(a[i])
