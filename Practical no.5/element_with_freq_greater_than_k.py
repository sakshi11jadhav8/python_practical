
# Python program to extract element with frequency greater than K ...!!

list1 = [4,3,3,4,4,4,5,5,6,7,8,8,9]
print('The original list is :' + str(list1))
k = 2
result = []
for i in list1:
    freq = list1.count(i)
    if freq > k and i not in result:
        result.append(i)

print("The required elements are :" + str(result))
        
