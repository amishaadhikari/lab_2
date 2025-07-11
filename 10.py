s=input("enter a sentence:")
v={'a','e','i','o','u'}
lower=s.lower()
unique=set()
for i in lower:
    if i in v:
        unique.add(i)
print(unique)
