
# Python program to remove the i th occurance of given word in a list where words repeated...!!

def RemoveNthWord(list, word, I):
    c = 0
    for i in range(0, len(list)):
        if(list[i] == word):
            c = c+1
            if(c == I):
                del(list[i])
                return True
    return False

list = ['opearting', 'system','and', 'operating', 'devices']
word = 'operating'
I = 3

temp = RemoveNthWord(list, word, I)

if(temp == True):
    print("Updated list is: ",list)
else:
    print("Item is not updated ")
