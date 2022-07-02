
# Python program to Sort the tuples by total digits

def count_digits(t):
    for x in t:
        return sum([len(str(x))])


l = [(1, 3, 45, 23), (4, 55, 7), (1, 3), (3, 44, 666, 111)]

print("Original list:", l)

l.sort(key=count_digits)

print("Sorted list:", l)
