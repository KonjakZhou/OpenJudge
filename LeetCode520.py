class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[:1].upper() == word[:1] and word[1:].lower() == word[1:]:
            return True
        return False

