import math
m=int(input("Enter the number that is greater than 6\n"))
n=0
def showNumbers(limit):
    if (limit>6):
        print("0 NILL")

        for i in range (1,limit+1):
            n=i
            if(i%math.sqrt(i)==0):
                print("{0} Square Number".format(n))
            else:
                print("{0} NOT a Square  Number".format(n))
showNumbers(m)



#Lucciffer
