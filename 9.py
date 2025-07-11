import random
n=set()
while (len(n)<10):
    n.add(random.randint(1,100))
print(n)
n.remove(max(n))
n.remove(min(n))
print("after removing smallest and largest elements:",n)