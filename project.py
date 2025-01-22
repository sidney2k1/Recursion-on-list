#write the program to find the length of a given array
def lengtharray(a):
    if not a:
        return 0
    return 1 + lengtharray(a[1::2]) + lengtharray(a[2::2])
a=[1,2,3,4,5,6]
print("Length of the list is:",lengtharray(a))
