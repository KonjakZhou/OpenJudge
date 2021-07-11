class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if len(envelopes) <= 1:
            return len(envelopes)

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        widths = [x[-1] for x in envelopes]
        d = [widths[0]]
        for i in range(1, len(widths)):
            if widths[i] > d[-1]:
                d.append(widths[i])
            else:
                index = self.biSearch(d, widths[i])
                d[index] = widths[i]

        return len(d)

    @staticmethod
    def biSearch(arr, target):
        def search(a, l, r, target):
            if l>=r:
                if a[l] >= target:
                    return l
                return l+1

            mid = (l+r)>>1
            if a[mid] == target:
                return mid
            if a[mid] > target:
                return search(a, l, mid-1, target)
            if a[mid] < target:
                return search(a, mid+1, r, target)
        return search(arr, 0, len(arr)-1, target)  
                

if __name__=="__main__":
    solution = Solution()
    # envelopes = [[5,4],[6,4],[6,7],[2,3]]
    # print(solution.maxEnvelopes(envelopes))
    
    envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
    print(solution.maxEnvelopes(envelopes))

