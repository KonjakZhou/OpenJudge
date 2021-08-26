class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        n = len(people)
        ans = n
        i = 0
        j = n-1
        while j>i:
            if people[i] + people[j] <= limit:
                ans -= 1 
                i += 1
                j -= 1
            else:
                j -= 1
        return ans 