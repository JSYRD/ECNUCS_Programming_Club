L = list(range(1,13,2))
print(L)
for i in range(0,len(L)):
    if(i==3):L.pop(1)
    print(L[i])