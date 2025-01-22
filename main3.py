def maxelementarray(a):
    length=len(a)
    if length==0 or length==1:
        return a[0]
    return max(a[0],maxelementarray(a[1:]))
a=[]
asize=int(input("Enter the size of the array:"))
for i in range(asize):
    n=int(input("Enter a number:"))
    a.append(n)
print("Max element in the array is:",maxelementarray(a))