#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mergeSort_sort(int *arr, int l, int q, int r){
	int tl,tr,tt;
	int tmp[r-l];
	
	tl = l;
	tr = q;
	for (tt=l; tt<r; tt++)
		if (tr>=r || (tl<q && arr[tl]<arr[tr])) {
			tmp[tt-l] = arr[tl];
			tl ++;
		}
		else {
			tmp[tt-l] = arr[tr];
			tr ++;
		}
	for (tt=l; tt<r; tt++)
		arr[tt] = tmp[tt-l];
	return ;	
}

void mergeSort(int *arr, int l, int r){
		
	if (r-l > 1) {
		int p = (l+r) >> 1;
		mergeSort(arr, l, p);
		mergeSort(arr, p, r);
		mergeSort_sort(arr, l, p, r);
	}
	
	return ;	
}

int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize){
	int *result;
	int cnt[1001];
	int position[1001];
	
	result = (int *)malloc(sizeof(int) * 1001);
	memset(result, 0, sizeof(int)*1001);
	memset(cnt, 0, sizeof(int)*1001;
	memset(position, -1, sizeof(int)*1001);
	
	int i,j;
		
	for (i=0;i<arr2Size;i++)
		position[arr2[i]] = i;
//	printf("\n%d\n", i);
	for (i=0;i<arr1Size;i++)
		if (position[arr1[i]]>=0) {
			cnt[arr1[i]] ++;
			arr1[i] = 32767;
		}
//	printf("\n%d\n", i);
	mergeSort(arr1, 0, arr1Size);
	
	int t=0;
	for (i=0;i<arr2Size;i++)
		for (j=0;j<cnt[arr2[i]]; j++){
			result[t] = arr2[i];
			t++;
		}                          
	
	for (i=0; i<arr1Size && arr1[i]<32767; i++){
		result[t] = arr1[i];
		t++;
	}
			
	*returnSize = arr1Size;
	printf("%d\n", *returnSize);
	return result;
}

int main(void){
	int arr1[11] = {2,3,1,3,2,4,6,7,9,2,19};
	int arr2[11] = {2,1,4,3,9,6};
	int arr1Size = 11;
	int arr2Size = 6;
	int i;
	int * result;

	result = relativeSortArray(arr1, arr1Size, arr2, arr2Size, &arr1Size);
	for (i=0; i<arr1Size; i++)
		printf("%d ", result[i]);
}
