class Solution:
    def verifyPostorder(self, postorder):
        def verify(postorder):
            n = len(postorder)
            if n<=1:
                return True
            
            flag = False
            root = postorder[-1]
            for bounder in range(n-2, -1, -1):
                if not self.cmp(postorder[bounder], root):
                    flag = True
                    break
            if flag:
                bounder += 1
            for i in range(bounder):
                if self.cmp(postorder[i], root):
                    return False
            return verify(postorder[:bounder]) and verify(postorder[bounder:-1])

        if len(postorder)<=3:
            return True
        if postorder[-2]>postorder[-1]:
            self._dir = True
        else:
            self._dir = False
        return verify(postorder)
        
    
    def cmp(self,a,b):
        if self._dir:
            return a>b
        return a<b

if __name__=="__main__":
    # postorder = [1,2,5,10,6,9,4,3]
    postorder = [1,2,3,4,5]
    solution = Solution()
    print(solution.verifyPostorder(postorder))
