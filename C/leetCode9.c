#include<stdio.h>

int isPalindrome(int x){
	int half=0;
	
	if (x<0) return 0;
	if (x==0) return 1;
	if (x%10 == 0) return 0;
	
	while (x>half)
	{
		half = half * 10 + x%10;
		x = x/10;
	}
	
	if (half > x)
		half = half/10;
	
	if (half==x) 
		return 1;
	return 0;
}

int main(void)
{
	int x = 100;
	printf("%d", isPalindrome(x));
}
