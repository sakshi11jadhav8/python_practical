
# Python Program to count unique value inside the list...!!

list1 = [1,1,2,3,4,5,5,6,7]
l2 = []
count = 0
for item in list1:
    if item not in l2:
        count += 1
        l2.append(item)
print("No of unique items in list are :",count)
