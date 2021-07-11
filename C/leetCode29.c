#include<stdio.h>

int divide(int dividend, int divisor){
	int flag = 0;
	
	long long longDividend = dividend;
	long long longDivisor = divisor;
	
	if (longDividend==0) return 0;
	if (longDividend<0 && longDivisor>0)
	{
		flag = 1;
		longDividend = -longDividend;
	}
	if (longDividend>0 && longDivisor<0)
	{
		flag = 1;
		longDivisor = -longDivisor;
	}
	if (longDividend<0 && longDivisor<0)
	{
		longDivisor = -longDivisor;
		longDividend = -longDividend; 
	}
	long long ans = 0;
	long long maxlongint = 2147483647;
	long long a,b;
	
	while (longDividend >= longDivisor)
	{
		a = longDivisor;
		b = 1;
		while ((longDividend ^ a) > a)
			if ((a<<1) < longDividend)
			{
				a = a<<1;
				b = b<<1;
			}
			else break;
		
		ans += b;
		longDividend = longDividend - a;
	}
	
	if (flag) ans = -ans;
	if (ans < -maxlongint-1 || ans > maxlongint) 
		return maxlongint;
	return ans;
}

int main(void)
{
	int dividend = -1;
	int divisor = -1;
	printf("%d", divide(dividend,divisor));
}

