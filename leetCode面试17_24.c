#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* getMaxMatrix(int **matrix, int matrixSize, int* matrixColSize, int* returnSize)
{
	int *ans = (int *)malloc(sizeof(int) * 4);
	int maxAns = -2147483648;
	int M=matrixSize, N=*matrixColSize;
	int (*Matrix)[N];
	int i,j,k;	
	
	int colSum[M+1][N];
	int d[N];
	int s[N];
	memset(colSum, 0, sizeof(int)*M*N);
	
	
	Matrix = matrix;
	for (i=0; i<M; i++)
	{
		for (j=0; j<N; j++)
		{
			colSum[i+1][j] = colSum[i][j] + Matrix[i][j];
		}
	}
	
	for (i=0; i<M; i++)
	{
		for (j=i+1; j<M+1; j++)
		{
			memset(d, 0, sizeof(int) * N);
			memset(s, 0, sizeof(int) * N);
			d[0] = colSum[j][0] - colSum[i][0];
			s[0] = 0;
			for (k=1; k<N; k++)
			{
				d[k] = colSum[j][k] - colSum[i][k];
				if (d[k] + d[k-1] > d[k])
				{
					d[k] = d[k] + d[k-1];
					s[k] = s[k-1];
				}
				else
				{
					s[k] = k;
				}
			}
			
			for (k=0; k<N; k++)
			{
				if (d[k] > maxAns)
				{
					ans[0] = i;
					ans[1] = s[k];
					ans[2] = j-1;
					ans[3] = k;
					maxAns = d[k];
				}
			}
		}
	}	
	
	*returnSize = 4;
	return ans;
}

int main(void)
{
	int matrixSize = 2;
	int matrixColSize = 2;
	int matrix[matrixSize][matrixColSize];
	
	int input[100][100] = {{0, -1}, {-1, 0}};
	
	int returnSize;
	int i,j;
	
	for (i=0 ; i<matrixSize; i++)
	{
		for (j=0; j<matrixColSize; j++)
		{
			matrix[i][j] = input[i][j];
		}
	}
	int * ans = getMaxMatrix((int **)matrix, matrixSize, &matrixColSize, &returnSize);
	
	for (i=0; i<returnSize; i++)
	{
		printf("%d ", ans[i]);
	}	
}
