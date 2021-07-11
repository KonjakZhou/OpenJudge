#include<stdio.h>

int reverse(int x){
	long long y = x;
	long long maxint = 2147483647;
	long long ans = 0;
	int flag = 0;
	
	if (y<0)
	{
		flag = 1;
		y = -y;
	}
	
	while (y>0)
	{
		ans = ans *10 + y%10;
		y = y/10;
	}
	
	if (flag)
		if (ans > maxint+1)
			return 0;
		else
			return -ans;
	else
		if (ans > maxint)
			return 0;
		else return ans;
}

int main(void)
{
	printf("%d", reverse(-2147483647)); 
}


