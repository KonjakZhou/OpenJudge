#include<stdio.h>
#include<string.h>

int isAnagram(char * s, char * t)
{
	int lens = strlen(s);
	int lent = strlen(t);
	
	if (lens != lent)
	{
		return 0;
	}
	
	int flag[26];
	memset(flag, 0, sizeof(flag));
	
	int i;
	for (i=0; i<lens; i++)
	{
		flag[s[i]-'a'] ++;
		flag[t[i]-'a'] --;
	}
	for (i=0; i<26; i++)
	{
		if (flag[i] != 0)
		{
			return 0;
		}
	}
	
	return 1;
}

int main(void)
{
	char s[10] = "anagram";
	char t[10] = "nagaram";
	int ans = isAnagram(s, t);
	printf("%d", ans);
} 
