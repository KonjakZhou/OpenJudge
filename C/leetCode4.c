#include<stdio.h> 

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
	if (nums1Size + nums2Size == 1)
		if (nums1Size)
			return nums1[0];
		else
			return nums2[0]; 
	
	int i,j,t;	
	int num1,num2;
	int k = (nums1Size + nums2Size +1) >> 1;
	
	i = 0;
	j = 0;
	t = 0;
	num1=0;
	num2=0;
	while (t<=k)
	{
		num1 = num2;
		if (j>=nums2Size || i<nums1Size && nums1[i]<nums2[j])
		{
			num2 = nums1[i];
			i++;
		}
		else
		{
			num2 = nums2[j];
			j++;
		}
		t++;
	}
	

	if ((nums1Size + nums2Size) % 2 == 1)
		return num1;
	return (num1+num2)/2.0;
	
}

int main(void)
{
	int nums1[0];
	int nums2[1]={1};
	printf("%lf", findMedianSortedArrays(nums1, 0, nums2, 1));
	return 0;
}
