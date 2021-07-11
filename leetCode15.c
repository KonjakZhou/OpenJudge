#include<stdio.h>

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
	int **ans;
	int l,r,k;
	int t;
	
	ans = (int **)malloc(sizeof(*ans) * 17000);
	for (l=numsSize-1;l>0; l--)
		for (r=0; r<l; r++)
			if (nums[r]>nums[r+1])
			{
				t = nums[r];
				nums[r] = nums[r+1];
				nums[r+1] = t;
			}

	*returnSize = 0;
	for (k=0; k< numsSize-2 && nums[k]<=0 ; k++)
	{
		
		l = k+1; 
		r = numsSize -1;
		
		while (l<r)
		{
			int sum = nums[k] + nums[l] + nums[r];
			if (sum == 0)
			{
				ans[*returnSize] = (int*) malloc(sizeof(int) * 3);
				ans[*returnSize][0] = nums[k];
				ans[*returnSize][1] = nums[l];
				ans[*returnSize][2] = nums[r];
				
				*returnSize += 1;
				
				do r--; while (nums[r]==nums[r+1] && l<r);
				do l++; while (nums[l]==nums[l-1] && l<r);
				
			}
			else
			if (sum < 0)
				l++;
			else r--;
		}
		
		while (nums[k] == nums[k+1] && k<numsSize-2) k++; 
		
	}
	
	*returnColumnSizes = (int *)malloc( sizeof(int) * (*returnSize));
	for (k=0;k<*returnSize; k++) 
		(*returnColumnSizes)[k] = 3; 
	return ans;	
	
}

int main(void)
{
	int nums[] = {-2,0,1,1,2};
	int numsSize = 5;
	int returnSize;
	int *returnColumnSizes;
	
	int **ans = threeSum(nums, numsSize, &returnSize, &returnColumnSizes);  
	
	int i,j;
	
	for (i=0; i<returnSize; i++)
	{
		for (j=0; j<returnColumnSizes[i]; j++)
			printf("%d ", ans[i][j]);
		printf("\n");
	}
}
