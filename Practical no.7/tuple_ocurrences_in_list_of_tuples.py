# Python program to Count tuple occurences in a list of tuples

def count_t(l):
    d = {}

    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])


l = [(1, 2, 2), (2, 3), (1, 2, 3), (3, 5), (1, 2, 3), (3, 5)]


count_t(l)
