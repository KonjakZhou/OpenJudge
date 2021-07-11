class Solution:
    def searchMatrix(self, matrix, target):
        def biSearch(test, l, r, target):
            while l<=r:
                mid = (l+r)>>1
                if test[mid] == target:
                    return mid
                if test[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            return r
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        colList = [matrix[i][0] for i in range(m)]
        rownumber = biSearch(colList, 0, m-1, target)
        if target==matrix[rownumber][0]:
            return True
        colnumber = biSearch(matrix[rownumber], 0, n-1, target)
        if target==matrix[rownumber][colnumber]:
            return True
        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    solution = Solution()
    print(solution.searchMatrix(matrix, target))