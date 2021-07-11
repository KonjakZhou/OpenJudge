#include<stdio.h>
#include<string.h>

 char * longestCommonPrefix(char ** strs, int strsSize){
	char *ans;
	
	int k,i;
	int maxlen = strlen(strs[0]);
	for (k=1;k<strsSize;k++)
	{
		for (i=0;i<maxlen; i++)
			if (strs[0][i]!=strs[k][i])
			{
				if (i==0) return "";
				if (maxlen > i) maxlen = i;
				break;
			}
	}
	ans = (char*) malloc(maxlen+1);
	memcpy(ans, strs[0], maxlen);
	ans[maxlen] = '\0';
	return ans;
}

int main(void)
{
	char *s[10];
	s[0] = "";
	printf("%s", longestCommonPrefix(s,0));
	
	return 0;
}
