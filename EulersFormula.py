import math
n=int(input("Enter the value of n in Euler's formula: "))
sum1=1
for i in range(1,n+1):
    sum1=sum1+(1/math.factorial(i))
print("value of e is :",round(sum1,2))

#Lucciffer
