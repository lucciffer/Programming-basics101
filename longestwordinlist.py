n = int(input("Enter the total words in list"))
list=[0 for i in range (n)]
for i in range (0,n):
  list[i]=str(input())

def longestoflist(list):
    max=0
    for i in range (0,n):
        if (len(list[i]) >= max):
            max=len(list[i])
    print("length of longest word in list is {0}".format(max))
longestoflist(list)



#Lucciffer
