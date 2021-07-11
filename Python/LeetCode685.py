class Solution:
    def findRedundantDirectedConnection(self, edges):
        def getAncestor(x, father):
            if x == father[x]:
                return x
            return getAncestor(father[x], father)
        
        def isUnion(x, y, father):
            xAncestor = getAncestor(x, father)
            yAncestor = getAncestor(y, father)
            if xAncestor == yAncestor:
                return True
            return False

        def union(x, y, father):
            father[y] = x
            return 

        n = 0
        for edge in edges:
            if n < edge[0]:
                n = edge[0]
            if n < edge[1]:
                n = edge[1]
        father = [i for i in range(n+1)]

        isDoubleIn = False
        isCircle = False
        for edge in edges:
            if father[edge[1]]!=edge[1]:
                last_edge = (father[edge[1]], edge[1])
                next_edge = (edge[0], edge[1])
                father[edge[1]] = edge[1]
                isDoubleIn = True
            else:
                if not isCircle:
                    if isUnion(edge[0], edge[1], father):
                        circle_edge =  edge
                union(edge[0], edge[1], father)
            
        if isDoubleIn:
            if isUnion(last_edge[0], last_edge[1], father):
                return last_edge
            return next_edge
        return circle_edge

if __name__=="__main__":
    edges = [[1,2],[1,3],[2,3]]
    edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
    # edges = [[2,1],[3,1],[4,2],[1,4]]
    edges = [[4,1],[1,5],[4,2],[5,1],[4,3]]
    solution = Solution()
    print(solution.findRedundantDirectedConnection(edges))