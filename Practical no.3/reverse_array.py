
# Python program to print the elements of array in reverse order...!!


arr = [1, 2, 3, 4, 5, 6]
print("Given original array is ")
for i in range(0,len(arr)):
    print(arr[i])
print("Array in reverse is ")
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
