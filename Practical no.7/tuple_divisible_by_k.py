
# Python program to Find tuple which has elements divisible by k...!!

t = []

k = int(input("Enter k: "))

for i in range(0, 50):
    if i % k == 0:
        t.append(i)

t=tuple(t)

print("Tuple of numbers divisible by", k)
print(t)
