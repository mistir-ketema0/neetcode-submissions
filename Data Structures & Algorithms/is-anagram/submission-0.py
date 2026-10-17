class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = []
        if len(s) != len(t):
            return False
        for i in s:
            first_word.append(i)

        for j in t:
            if j in first_word:
                first_word.remove(j)
            if len(first_word) == 0:
                return True
        return False
                    

        