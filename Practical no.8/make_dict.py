
# Python program in wich Two lists are given (one has key & other has values). merge them & make a dictionary

combined_dict = {}

keys = ["key1","key2","key3"] 
values = ["val1","val2","val3"]

for k,v in zip(keys,values):
    combined_dict[k] = v

print(combined_dict)
