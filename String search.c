
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[20];    char search[20];    
    int count1,count2,i,j,flag=0;
    scanf("%s",str); 
    scanf("%s",search); 

    count1 = strlen(str);
    count2 = strlen(search);
    
 
    for (i = 0; i <= count1 - count2; i++)
    {
        for (j = i; j < i + count2; j++)
        {
            flag = 1;
            if (str[j] != search[j - i])
            {
                flag = 0;
                break;
            }
        }
        if (flag == 1)
            break;
    }
    if (flag == 1)
        printf("Present\n");
    else
        printf("Absent\n");
 
    return 0;
}
