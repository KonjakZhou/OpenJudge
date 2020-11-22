#include<stdio.h>

int threeSumClosest(int* nums, int numsSize, int target){
	int ans,sub=2147483647;
	int l,r,k;
	int t;
	
	for (l=numsSize-1;l>0; l--)
		for (r=0; r<l; r++)
			if (nums[r]>nums[r+1])
			{
				t = nums[r];
				nums[r] = nums[r+1];
				nums[r+1] = t;
			}

	for (k=0; k< numsSize-2; k++)
	{
		
		l = k+1; 
		r = numsSize -1;
		
		while (l<r)
		{
			int sum = nums[k] + nums[l] + nums[r];
			if (sum == target)
				return sum;
			else
			if (sum < target)
			{
				if (sub> (target-sum))
				{
					ans = sum;
					sub = target-sum;
				}
				do l++; while (nums[l]==nums[l-1] && l<r);
			}	
			else 
			{
				if (sub> (sum-target))
				{
					ans = sum;
					sub = sum-target;
				}
				do r--; while (nums[r]==nums[r+1] && l<r);
			}
		}
		
		while (nums[k] == nums[k+1] && k<numsSize-2) k++; 
		
	}
	
	return ans;	
	
}

int main(void)
{
	int nums[] = {-2,0,1,1,2};
	int numsSize = 5;
	int target = 5;
	
	int ans = threeSumClosest(nums, numsSize, target);
	
	printf("%d" , ans);
}
