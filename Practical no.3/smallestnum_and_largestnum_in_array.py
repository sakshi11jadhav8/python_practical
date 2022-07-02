
#Python program to print the largest and smallest element in an array...!!

arr = [10, 34, 21, 7, 43, 8, 13]
smallest = arr[0]
largest = arr[0]
for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
    if arr[i] > largest:
        largest = arr[i]
print(smallest)
print(largest)
