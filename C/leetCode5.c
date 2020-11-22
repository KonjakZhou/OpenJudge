#include<stdio.h>
#include<string.h>

char * longestPalindrome(char * s){
	int maxi,maxj,max=0;
	int len = strlen(s);
	int i,j,k;
	
	for (k=0; k<len; k++)
	{
		for (i=k,j=k; i>=0&&j<len; i--,j++)
			if (s[i] == s[j] && max<(j-i+1))
			{
				max = j-i+1;
				maxi = i;
				maxj = j;
			}
			else if (s[i]!=s[j]) break;
		
		for (i=k,j=k+1; i>=0&&j<len; i--,j++)
			if (s[i] == s[j] && max<(j-i+1))
			{
				max = j-i+1;
				maxi = i;
				maxj = j;
			}
			else if (s[i]!=s[j]) break;
	}
	
	char *ans = (char*)malloc(max+1);
	memcpy(ans, s+maxi, max);
	ans[max] = '\0';
	return(ans);
}

int main(void)
{
	char *s="babad";
	printf("%s", longestPalindrome(s));
}

 
