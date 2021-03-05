class Solution:
    def findRedundantConnection(self, edges):
        def getAncestor(x, father):
            if x == father[x]:
                return x
            father[x] = getAncestor(father[x], father)
            return father[x]

        def union(x, y, father):
            xAncestor = getAncestor(x, father)
            yAncestor = getAncestor(y, father)

            father[yAncestor] = xAncestor
            return
        
        def isUnion(x, y, father):
            xAncestor = getAncestor(x, father)
            yAncestor = getAncestor(y, father)
            
            if xAncestor == yAncestor:
                return True
            return False
        
        n = 0
        for edge in edges:
            if n < edge[0]:
                n = edge[0]
            if n < edge[1]:
                n = edge[1]
        father = [i for i in range(n+1)]

        for edge in edges:
            if isUnion(edge[0], edge[1], father):
                return edge
            union(edge[0], edge[1], father)