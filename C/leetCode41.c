#include<stdio.h>
#include<math.h>


int firstMissingPositive(int* nums, int numsSize){
	int i;
	for (i=0;i<numsSize;i++)
		if (nums[i]<=0)
			nums[i] = numsSize+1;
	
	for (i=0;i<numsSize;i++)
	{
		int index = abs(nums[i]);
		if (index<=numsSize)
			if (nums[index-1]>0)
				nums[index-1] = -nums[index-1];
	}
	
	for (i=0;i<numsSize;i++)
		if (nums[i]>0)
			return i+1;
			
	return numsSize+1; 
			
}

int main(void)
{
	int nums[] = {3,4,-1,1};
	int numsSize = 4;
	printf("%d", firstMissingPositive(nums, numsSize));
}


