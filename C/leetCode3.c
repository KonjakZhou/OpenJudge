#include<stdio.h>
#include<string.h>

int lengthOfLongestSubstring(char * s){
	int len = strlen(s);
	int i, k;
	int max = 0;
	int flag[256];
	
	memset(flag, 255, sizeof(flag));
	
	flag[s[0]] = 0;
	
	i = 0;
	for (k=0; k<len; k++)
	{
		int j;
		for (j=k-1; j>=i; j--)
			if (s[j]==s[k])
			{
				i = j+1;
				break;
			}
			
		if (max < (k-i+1)) max = k-i+1;
	} 
	return max;
}

int main(void)
{
	char *s = "";
	printf("%d", lengthOfLongestSubstring(s));
}

