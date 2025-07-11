n=int(input("enter range of list: "))
l=[]
for i in range(n):
    num=int(input(f"enter number{i+1}:"))
    l.append(num)
l2=[]
e_l=list(range(0,len(l),2))
print(e_l)
for index in e_l:
    count=0
    for j in range(1,l[index]+1):
        if (l[index]%j==0):
            count+=1
    if(count==2):
        l2.append(l[index])
print(l2)