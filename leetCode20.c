#include<stdio.h>
#include<string.h>

int isValid(char * s){
	int len = strlen(s);
	char heap[len+1];
	char ch;
	int top = 0;
	int i;
	
	for (i=0;i<len;i++)
		switch (s[i])
		{
			case '(':
			case '[':
			case '{':
			{
				heap[top++] = s[i];
				break;
			}
			case ')':
			{
				if (top==0) return 0;
				ch = heap[--top];
				if (ch != '(') return 0;	
				break;
			}
			case ']':
			{
				if (top==0) return 0;
				ch = heap[--top];
				if (ch != '[') return 0;
				break;
			}
			case '}':
			{
				if (top==0) return 0;
				ch = heap[--top];
				if (ch != '{') return 0;
				break;
			}
			default : break;
		}
	
	if (top) return 0;
	return 1;
}

int main(void)
{
	char *s = "{[]}";
	printf("%d", isValid(s));
}


