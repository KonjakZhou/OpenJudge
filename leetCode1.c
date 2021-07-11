#include<stdio.h> 

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
	int i,j;
	int * returnArr = (int*)malloc(2 * sizeof(int));
	for (i=0; i<numsSize; i++)
		for (j=i+1; j<numsSize; j++)
			if (nums[i] + nums[j] == target)
			{
				returnArr[0] = i;
				returnArr[1] = j;
			}
	
	return returnArr;
} 

int main(void)
{
	int *a, *b;
	int nums[4] = {2, 7, 11, 15};
	int target = 9;
	
	
	a = twoSum(nums, 4, target, b);
	printf("%d %d", a[0], a[1]);
	return 0;
}
