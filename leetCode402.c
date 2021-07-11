#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * removeKdigits(char * num, int k)
{
	if (k<=0) return num;
	
	int numLen = strlen(num);
	char *stack = (char *)malloc(sizeof(char) * (numLen+1));
	
	stack[0] = num[0];
	int top = 0;
	
	int j;
	int cnt=k;
	int flag = 0;
	
	for (j=1; j<numLen; j++)
	{			
		if (top>=0 && !flag)
		{
			if (num[j]>=stack[top])
			{
				stack[++top] = num[j];
				continue;
			}
			while (num[j]<stack[top])
			{
				top --;
				cnt --;		
				if (cnt==0)
				{
					flag = 1;
				}
				if (cnt==0 || top<0)
				{
					break;
				}
			}
		}
		
		if (top>=0 || top<0 && num[j]>'0')
		stack[++top] = num[j];
	}
		
	while (top>=0 && cnt>0){
		
		top --;
		cnt --;
	}
	
	if (top<0)
	{
		stack[0] = '0';
		stack[1] = '\0';
	}
	else
		stack[++top] = '\0';	
	return stack;
}

int main(void){
	char num[7] = "10200";
	int k = 1;
	
	char * newNum = removeKdigits(num, k);
	printf("%s", newNum);
	return 0;
} 
