s=input("enter a text:")
d={}
l=s.lower()
for i in l:
    if i.isalpha():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
for i,count in d.items():
    print(f"{i}:{count}",end=" ")