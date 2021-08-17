class Solution:
    def checkRecord(self, s):
        count_A = 0
        count_L = 0
        
        for i, ch in enumerate(s):
            if i == 0 :
                if ch == 'A':
                    count_A += 1
                elif ch == 'L':
                    count_L += 1
            else:
                if ch == 'L':
                    if s[i-1] == 'L':
                        if count_L == 2:
                            return False
                    count_L += 1
                    
                else:                        
                    if ch == 'A':
                        if count_A == 1:
                            return False
                        count_A += 1
                    count_L = 0
        return True
