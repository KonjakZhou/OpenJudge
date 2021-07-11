class Solution:
    def hIndex(self, citations):
        citations.sort(reverse = True)
        for index, value in enumerate(citations):
            if index >= value:
                return index
        return len(citations)


if __name__ == '__main__':
    solution = Solution()

    citations = [3,0,6,1,5]
    print(solution.hIndex(citations))