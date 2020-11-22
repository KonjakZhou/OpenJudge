#include<stdio.h>
#include<string.h>

int main(void)
{
	int a[100];
	
	memset(a,255,sizeof(a));
	
	printf("%d", a[0]);	
}
