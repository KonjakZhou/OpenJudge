#include<stdio.h>
#include<string.h>


void dfs(int k, char **ans, int *returnSize, char* digits, int digitsLen ,char **f, char *temp)
{
	int i,l,currDigit;
	if (k==digitsLen)
	{
		
		temp[k] = '\0';
		ans[*returnSize] = (char *)malloc(sizeof(char) * (k+1));
		strcpy(ans[(*returnSize)++], temp);
		return ;
	}
		
	currDigit = digits[k]-48;
	l = strlen(f[currDigit]);
	for (i=0;i<l;i++)
	{
		temp[k] = f[currDigit][i];
		dfs(k+1, ans, returnSize, digits, digitsLen, f, temp);
	}
}

char ** letterCombinations(char * digits, int* returnSize){
	char *f[10];
	f[2] = "abc";
	f[3] = "def";
	f[4] = "ghi";
	f[5] = "jkl";
	f[6] = "mno";
	f[7] = "pqrs";
	f[8] = "tuv";
	f[9] = "wxyz";
	
	char **ans = (char **)malloc(sizeof(char *) * 10000);
	char temp[100];
	int digitsLen = strlen(digits);
	
	*returnSize = 0;
	if (digitsLen)
		dfs(0, ans, returnSize, digits, digitsLen, f, temp);
	return ans;
}

int main(void)
{
	char *digits = "23";
	int returnSize;
	char **ans = letterCombinations(digits, &returnSize);
	int i;

	for (i=0;i<returnSize;i++)
		printf("%s\n", ans[i]);
}
