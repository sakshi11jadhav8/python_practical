

# Program to find the intersection of two list ..!!

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
final_list=[]
for i in range(0,len(list1)):
    if(list1[i]==list2[i]):
        final_list.append(list1[i])

print("intersection of two list is :",final_list)
    
