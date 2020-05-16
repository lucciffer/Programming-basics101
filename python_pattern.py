from __future__ import print_function
n = int(input("Enter the number: "))
for i in range(n, 0, -1):
    for j in range(-n+1,n):
        if(n-abs(j)<=i):
            print(n-abs(j),end="")
        else:
            print(" ",end="")
    print("")
