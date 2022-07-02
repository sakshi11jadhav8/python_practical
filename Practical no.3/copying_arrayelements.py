
# Python program to copy all elements of one array into another...!!

arr1 = [10, 20, 30, 40, 60, 80]
arr2 = [None]*len(arr1)
for i in range(0,len(arr1)):
    arr2[i]=arr1[i]
print("Elements of original array is ")
for i in range(0,len(arr1)):
    print(arr1[i])
print()
print("Elements of new array ")
for i in range(0,len(arr2)):
    print(arr2[i])
