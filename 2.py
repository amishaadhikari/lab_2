l1=set([11,22,33,44,55])
l2=set([44,55,66,77,88])
merged= []
for i in l1:
    merged.append(i)
for j in l2:
    merged.append(j)
print("merged list",merged)
i=l1.intersection(l2)
for j in merged:
    if j in i:
        merged.remove(j)
print(merged)        