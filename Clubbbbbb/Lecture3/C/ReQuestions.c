#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define N 100
int main(){
    int a[N];
    memset(a,0,N);
    int r=0,y;
    do{scanf("%d",&a[r++]);}while(y=getchar()!='\n');
    int t=2;
    while(((a[t])-a[t-1]==a[t-1]-a[t-2])&&(t<r)) t++;
    if(t==r) printf("Yes");
    else printf("No");
    return 0;
}