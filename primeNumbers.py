n=int(input("Enter the limit:"))
def prime(limit):
    
    
 for limit in range (0,limit+1):
    if limit>1:
      for i in range (2,limit):
         if limit % i==0:
               break
      else :
        print(limit)
print("The prime numbers are")        
prime(n)



#Lucciffer
