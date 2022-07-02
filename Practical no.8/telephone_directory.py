
# Make telephone directory: 1. Find value. 2. replace value. 3. Replace key.

def find_num(name):
    print(name, ":", d[name])


def replace_num(name, num):
    d[name] = num
    print("Contact updated!\n", name, ":", d[name])


def replace_name(name, num):
    for key, value in d.items():
        if num == value:
            d[name] = d[key]
            del d[key]
            break
    print("Contact updated!\n", name, ":", d[name])


d = {'Mirabel': 9101443214,
     'Isabela': 9325544335,
     'Bruno':   7853232315,
     'Luisa':   9446584852,
     'Dolores': 8654448632,
     }

find_num('Bruno')
replace_num( 'Luisa', 8632436547)
replace_name( 'Isa', 9325544335)
