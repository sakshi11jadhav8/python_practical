
# Python program to Sort dictionary by key and value...!!

dict = {'aman': 10,
        'rajnish': 9,
        'sanjeev': 15,
        'yash': 2,
        'manan': 32}

print("Sorted by key:")
print(sorted(dict.items(), key=lambda kv: (kv[0], kv[1])))

print("\nSorted by value:")
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))
