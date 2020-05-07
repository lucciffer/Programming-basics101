#include<stdio.h>
int main()
 {
float x,p=1;
float s=0,i=1,n;
printf("Enter the number whose factorial is to be found out\n" );
scanf("%f",&x );
if(x>0)
{
  while(x>=1)
  {
    p=p*x;
    x--;
  }
  printf("The factorial of the number is%f\n", p );
  printf("Enter the upper limit\n" );
  scanf("%f",&n );
  while(i<=n)
{
  s=s+1/i;

}
printf("sum=%f",s );
}
  return 0;
}
