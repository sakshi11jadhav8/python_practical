#Python program to Count occurrence of given word in given sentence...!!

def count_x(s, x):
    count = 0
    words = list(s.lower().split())
    for i in words:
        if i == x:
            count += 1
    print(("'{}' occurred {} times").format(x, count))


s = "Twinkle twinkle little star"
count_x(s, 'twinkle')
