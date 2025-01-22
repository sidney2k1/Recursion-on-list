def totalarraysum(a):
    length=len(a)
    if length==0 or length ==1:
        return a[0]
    return a[0]+ totalarraysum(a[1:])
asize=int(input("Enter the size of the set:"))
a=[]
for i in range(asize):
    n=int(input("enter a number:"))
    a.append(n)
print("array total sum=",totalarraysum(a))