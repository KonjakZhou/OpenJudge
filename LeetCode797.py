class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(s, aim):
            if s == aim:
                ans.append(path[:])
                return 
            for t in graph[s]:
                if flag[t]:
                    path.append(t)
                    flag[t] = False
                    dfs(t, aim)
                    flag[t] = True
                    path.pop()
        
        n = len(graph)
        if n == 0 :
            return []
    
        path = list()
        ans = list()
        flag = [True for _ in range(n)]
        flag[0] = False
        path.append(0)
        dfs(0, n-1)
        return ans 
