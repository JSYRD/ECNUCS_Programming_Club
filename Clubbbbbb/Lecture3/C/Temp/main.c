#include <stdio.h>
#include <stdlib.h>

int my_add(int a, int b){
    int c;
    c=a+b;
    return c;
}
int main()
{
    int a,b;
    a=1;
    b=2;
    printf("%d\n",my_add(a,b));
    return 0;
}
