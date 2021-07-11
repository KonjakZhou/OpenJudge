#include<stdio.h>
#include<string.h>


int myAtoi(char * str){
	
	long long maxlongint = 2147483647;
	int i,flag;
	long long ans=0;
	
	int len = strlen(str);
	for (i=0;i<len;i++)
		if (str[i]==' ')
			continue;
		else
		if (str[i]<='9' && str[i]>='0' || str[i]=='-' || str[i]=='+')
		{
			if (str[i]=='-')
			{
				flag = 1;
				i++; 
			}	
			else
			{
				if (str[i]=='+')
					i++; 
				flag = 0;
			}
			break;
		}
		else return 0;
	
	 for (;i<len;i++)
	 	if (str[i]<='9' && str[i]>='0')
	 	{
	 		ans = ans*10 + str[i]- '0';
	 		if (ans > maxlongint)
	 			if (!flag)
	 				return maxlongint;
	 			else
	 				return -(maxlongint+1);
	 	}
	 	else break;
	
	if (flag)
		return -ans;
	return ans;
}

int main(void)
{
	char *s="91283472332";
	printf("%d", myAtoi(s));
}

