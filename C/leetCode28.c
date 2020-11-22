#include<stdio.h>
#include<string.h>

int strStr(char * haystack, char * needle){
	int i,j;
	int lenh = strlen(haystack);
	int lenn = strlen(needle);
	
	if (lenn == 0) return 0;
	for (i=0;i<=lenh-lenn;i++)
	{
		for (j=0; j<lenn && haystack[i+j] == needle[j]; j++);
		if (j==lenn) return i;
	}
	return -1;
}

int main(void)
{
	char * s = "aaaaa";
	char * n = "ll";
	printf("%d", strStr(s,n));
	return 0;
}
