#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXSIZE 100000000
int atoi(char s[])
{
    int i;
    int n=0;
    for(i=0;s[i]>='0'&&s[i]<='9';i++){
        n = n*10+(s[i]-'0');
    }
    return n;
}
int main(){
    char *s = (char*)malloc(sizeof(char)*MAXSIZE);
    int n;
    scanf("%s",&s);
    n = atoi(s);
    printf("%d",n);
    return 0;
}