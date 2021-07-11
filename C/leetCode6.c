#include<stdio.h>
#include<string.h>

char * convert(char * s, int numRows){
	int len = strlen(s);
	
	if (len == 0 || numRows==1) return s;
	 
	char rows[numRows][len];
	int rowLen[numRows];

	memset(rows, 0, sizeof(rows));
	memset(rowLen, 0, sizeof(rowLen));
	
	int i;
	int dirc = 1;
	int currRow = 0;
	
	for (i=0;i<len;i++)
	{
		rows[currRow][rowLen[currRow]++] = s[i];

		if (currRow == 0) dirc = 1;
		if (currRow == numRows-1) dirc = -1;
		currRow = currRow + dirc;	
	} 
	
	memset(s, 0, len);
	
	
	for (i=0;i<numRows;i++)
		strcat(s,rows[i]);
	return s;
	
}


int main(void)
{
	
	char s[1000] = "AAA";
	int numRows = 5;	
	printf("%s", convert(s,numRows));
	
} 
