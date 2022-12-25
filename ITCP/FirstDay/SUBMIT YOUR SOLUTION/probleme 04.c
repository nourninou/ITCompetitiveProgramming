#include<stdio.h>
int main(){
int arr1[100],arr2[100];
int i,j,n,m;
do{
printf("donner n\n");scanf("%d\n",&n);}
while(n<0||n>100);
for ( i = 0; i < n; i++)
{
    printf("donner arr1[%d]=%d\n",i+1,arr1);scanf("%d",&arr1);
    printf("arr1[%d]=%d",i+1,arr1);
}
for ( j = 0; j < m; j++)
{
    printf("donner arr2[%d]=%d\n",j+1,arr2);scanf("%d",&arr2);
    printf("arr2[%d]=%d",j+1,arr2);
}
j=0;
for ( i = 0; i < n; i++){
if(arr2[j]<arr1[i]){arr1=arr2};j++;
}
for ( i = 0; i < n; i++)
{
    printf("arr1[%d]=%d",i+1,arr1)
}
for ( j = 0; j < m; j++)
{
    printf("arr2[%d]=%d",j+1,arr2);
}


    return 0;
}