class Solution:
    def findCircleNum(self, isConnected):
        def getAncestor(x, father):
            ans = x
            while (father[ans] != ans):
                ans = father[ans]
                father[x] = ans
            return ans
        
        def union(x,y, father):
            xAncestor = getAncestor(x, father)
            yAncestor = getAncestor(y, father)
            father[yAncestor] = xAncestor
                
            return 

        n = len(isConnected)
        father = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]==1:
                    union(i,j, father)
        
        flag = [0 for _ in range(n)]
        for i in range(n):
            flag[getAncestor(i, father)] = 1
        
        ans = 0
        for i in range(n):
            ans += flag[i]

        return ans 

if __name__ == "__main__":
    isConnected = [
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        ]

    solution = Solution()
    print(solution.findCircleNum(isConnected))

