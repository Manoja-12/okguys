from array import*
n=int(input("Enter size of array\n"))
arr=list(map(int,input("Enter elements of array\n").split()))
arr.sort()
print("Ascending order array")
print(*arr)
