

list1 = [1,2,3,4,5]
dict1={1:2,2:3,3:4}
frz  = frozenset(dict1)
frzList = frozenset(list1)
for iter in frz:
    print(iter)
print(frzList)
for iter in frzList:
    print(iter)



tupl = (1,2,3,4,5,'1')

frzTup = frozenset(tupl)
print(frzTup)
for iter in frzTup:
    print(iter)


# Not possible
# frzDub = frozenset(list1, dict1)
# error 2 args given 1 expected



