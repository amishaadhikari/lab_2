n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    num=int(input(f"enter number{i + 1}: ") )
    l.append(num)
max=l[0]
min=l[0]
for number in l:
    if(max < number):
        max=number
    if(min > number):
        min=number
print(f"maximum number={max} minimnum number={min}")
for i in range(n):
    for j in range(i+1, n):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
print('sorted element:',l)
u=[]
for num in l:
    if num not in u:
        u.append(num)
print("unique elements:",u)