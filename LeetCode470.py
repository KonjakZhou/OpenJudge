# The rand7() API is already defined for you.
import random
def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        x = (rand7() - 1) * 7 + rand7()
        while x > 40:
            x = (rand7() - 1) * 7 + rand7()
        return (x -1) // 4 + 1

        