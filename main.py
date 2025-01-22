def checksorted(a):
    #calculate length of array
    length=len(a)
    #if length of the array is 0 or 1 it means there is no need to check if it is sorted
    if length==0 or length==1:
        return True
    return a[0]<=a[1] and checksorted(a[1:])
a=[1,2,3,4,5,6,8]
if checksorted(a):
    print("The list:",a,"is already sorted")
else:
    print("The list:",a,"is not sorted")


