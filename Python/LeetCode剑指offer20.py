class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        cur = 0
        for ch in s:
            if cur == 0:
                if ch=='+' or ch=='-':
                    cur = 1
                    continue
                if 48 <= ord(ch) <= 57:
                    cur = 2
                    continue
                if ch =='.':
                    cur = 3
                    continue
                return False
            if cur == 1:
                if 48 <= ord(ch) <= 57:
                    cur = 2
                    continue
                return False
            if cur == 2:
                if 48 <= ord(ch) <= 57:
                    continue
                if ch == '.':
                    cur = 3
                    continue
                if ch == 'e' or ch =='E':
                    cur = 4
                    continue
                return False
            if cur == 3:
                if 48 <= ord(ch) <= 57:
                    continue
                if ch == 'e' or ch =='E':
                    cur = 4
                    continue
                return False
            if cur == 4:
                if ch=='+' or ch=='-' or 48 <= ord(ch) <= 57:
                    cur = 5
                    continue
                return False
            if cur == 5:
                if 48 <= ord(ch) <= 57:
                    continue
                return False
                
        
        return True
        
if __name__=="__main__":
    pass