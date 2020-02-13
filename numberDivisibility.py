n=int(input("Enter the number:"))
def prime(n):
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1

    if (flag==0):
       print("{0} is prime ".format(n))
    else:
       if (n%3==0):
         print("{0} is divisible by 3 ".format(n))
       elif (n%7==0):
         print("{0} is divisible by 7 ".format(n))
       elif (n%9==0):
         print("{0} is divisible by 9 ".format(n))
       elif (n%11==0):
         print("{0} is divisible by 11 ".format(n))
       else :
         print("{0} is not divisible by 3,7,9,11 ".format(n))
prime(n)



#Lucciffer
