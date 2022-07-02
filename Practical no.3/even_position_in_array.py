
# Python program to print elements of an array present on even position...!!

arr = [ 12, 24, 32, 13, 45, 76]
print("original array is ")
for i in range(0,len(arr)):
    print(arr[i])
print("Elements in evven position of array is ")
for i in range(1,len(arr),2):
    print(arr[i])
