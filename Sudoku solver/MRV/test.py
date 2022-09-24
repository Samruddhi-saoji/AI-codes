from copy import deepcopy

list = [1 ,2 ,3 , 4]

def fun(list) :
    list.append(5)   #pass by reference
    list.remove(2)
    list.remove(3)
    return list



def printlen(x) :
    length = len(x)
    return length

print(fun(deepcopy(list)))  #### pass by reference
print( printlen(fun(deepcopy(list))))

print(list)
print(printlen(list))