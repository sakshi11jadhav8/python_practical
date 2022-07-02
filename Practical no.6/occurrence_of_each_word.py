# 5. Count occurrence of each word in given sentence

def count_x(s):
    words = list(s.lower().split())

    d = {}

    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])


s = "Twinkle twinkle little star"
count_x(s)
