#include<stdio.h>

int removeDuplicates(int* nums, int numsSize){

	int i,k;
	for (k=0;k<numsSize-1;k++)
		if (nums[k] == nums[k+1])
		{
			for (i=k; i<numsSize-1; i++)
				nums[i] = nums[i+1];
			numsSize --;
			k--;
		}
	return numsSize;
			
}


int main(void)
{
	int nums[] = {1,2,3,3,3,4,4,5};
	int numsSize = 8;
	
	int newLen = removeDuplicates(nums, numsSize);
	int i;
	for (i=0;i<newLen;i++)
		printf("%d ", nums[i]);
}
