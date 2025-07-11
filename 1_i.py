#using bulit-in functions
n=int(input("enter the number of elements in list:"))
l=[]
for i in range(n):
    num=int(input(f"enter number{i + 1}: ") )
    l.append(num)
print("maximum number:",max(l))
print("minimum number:",min(l))
print("sorted list",sorted(l))
print("unique elements:",list(set(l)))