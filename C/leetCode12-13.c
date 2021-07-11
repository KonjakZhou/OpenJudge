#include<stdio.h>
#include<string.h>

char * intToRoman(int num){

	char base[] = "IXCM";
	char half[] = "VLD";
	int k = 0;
	char *ans = (char *) malloc(100);
	char t[100];
	int i;
	memset(ans, 0, 100);

	while (num>0)
	{
		int a = num%10;
		num = num/10;
		
		switch (a)
		{
			case 0:
			case 1:
			case 2:
			case 3:
				{
					for (i=0; i<a; i++)
						t[i] = base[k];
					t[i] = '\0';
					break;
				}
			case 4:
				{
					t[0] = base[k];
					t[1] = half[k];
					t[2] = '\0';
					break;
				}
			case 5:
			case 6:
			case 7:
			case 8:
				{
					t[0] = half[k];
					for (i=0;i<a-5;i++)
						t[i+1] = base[k];
					t[i+1] = '\0';
					break;
				}
			case 9:
				{
					t[0] = base[k];
					t[1] = base[k+1];
					t[2] = '\0';
				}
			default: break;
			
		}
		strcat(t,ans);
		strcpy(ans,t);
		k++;
	}
	
	return ans;
}



int romanToInt(char * s){
	int order[255];
	
	order['I'] = 1;
	order['V'] = 5;
	order['X'] = 10;
	order['L'] = 50;
	order['C'] = 100;
	order['D'] = 500;
	order['M'] = 1000;
	
	int i;
	int len = strlen(s);
	if (len == 0) return 0;
	if (len == 1) return order[s[0]];
	
	int ans = 0;
	for (i=0;i<len-1;i++)
		if (order[s[i]]>=order[s[i+1]])
			ans += order[s[i]];
		else
			ans -= order[s[i]];
	ans += order[s[i]];
	
	return ans;
			
}


int main(void)
{
	int i;
	
	for (i=0;i<4000;i++)
		if (romanToInt(intToRoman(i))==i)
			continue;
		else 
		{
			printf("%d", i);
			printf("%d", romanToInt(intToRoman(i)));
			break;
		}
}
