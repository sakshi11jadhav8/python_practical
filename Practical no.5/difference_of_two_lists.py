
# Python program to compute the difference between two lists...!!

l1 = [10, 15, 20, 25, 30, 35, 40]
l2 = [25, 40, 35]
l3 = []

for i in l1 + l2:
    if i not in l1 or i not in l2:
        l3.append(i)

print("List 1: ", l1)
print("List 2: ", l2)
print("Diffrence: ", l3)
