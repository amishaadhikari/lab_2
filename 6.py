n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    num=int(input(f"enter number{i + 1}: ") )
    l.append(num)
t=tuple(l)
avg=sum(t)/len(t)
print("mean=",avg)
s=sorted(t)
if(len(t)%2==0):
    n1= t[len(t)//2]
    n2= t[(len(t)//2)+1]
    median=(n1+n2)/2
else:
    median=len(t)//2
print("median:",median)
uniq_l = tuple(set(t))
counts = []
for n in uniq_l:
    counts.append(t.count(n))
max_freq = max(counts)
index_max = counts.index(max_freq)
print(index_max)
print(f'Mode: {uniq_l[index_max]}')