#include<stdio.h>

int maxArea(int* height, int heightSize){
	int l,r;
	int ans = 0;
	
	l = 0;
	r = heightSize-1;
	
	while (l<r)
	{
		int a = ((height[l]<=height[r])?height[l]:height[r]) * (r-l);
		if (ans < a) ans = a;
		if (height[l] <= height[r])
			l++;
		else
			r--;		 
	}
	
	return ans;
}

int main(void)
{
	int side[10] = {1,8,6,2,5,4,8,3,7};
	printf("%d", maxArea(side, 9));
}
