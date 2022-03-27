#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int cmp(const void*a ,const void*b){
    int x = *(int*)a;
    int y = *(int*)b;
    return x>y?1:-1;
}

int cmp(const void *a, const void *b){
    
}
int main(){
    int a[10] = {9,8,7,6,5,4,3,2,1,0};
    qsort(a,10,sizeof(int),cmp);
    for(int i=0;i<10;i++) printf("%d ",a[i]);
    return 0;
}