#include<stdio.h>

int removeElement(int* nums, int numsSize, int val){

	int k=0,i;
	int n = numsSize;
	for (i=0;i<numsSize;i++)
		if(nums[i] == val)
			n--;
		else
			nums[k++] = nums[i];
	return n;
}

int main(void)
{
	int nums[] = {1,2,3,3,3,4,4,5};
	int numsSize = 8;
	int val = 3;
	
	int newLen = removeElement(nums, numsSize, val);
	int i;
	for (i=0;i<newLen;i++)
		printf("%d ", nums[i]);
}
