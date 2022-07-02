
# Python program to concatenate the two given lists..!!

l1 = ['p', 'q']
l2 = [1, 2, 3, 4, 5]
l3 = []

for i in range(len(l1)):
    for j in range(len(l2)):
        temp = l1[i] + str(l2[j])
        l3.append(temp)

print("Concatenated list: " + str(l3))
