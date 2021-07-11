#include<stdio.h>
#include<stdlib.h>

void moveZeroes(int* nums, int numsSize){
	int i,j;
	
	for (i=0; i<numsSize && nums[i]!=0; i++);
	for (j=i; j<numsSize && nums[j]==0; j++);
	
	while (1)
	{		
		if (j>=numsSize) return ;
		
		nums[i] = nums[i] ^ nums[j];
		nums[j] = nums[i] ^ nums[j];
		nums[i] = nums[i] ^ nums[j];
		
		for (; i<numsSize && nums[i]!=0; i++);
		for (; j<numsSize && nums[j]==0; j++);
	} 
}

int main(void)
{
	int a[1000];
	int n,i;
	
	scanf("%d", &n);
	for (i=0; i<n; i++)
	{
		scanf("%d", a+i);
	}
	
	moveZeroes(a, n);
	
	for (i=0; i<n; i++)
	{
		printf("%d ", a[i]);
	}
	return 0;
}
