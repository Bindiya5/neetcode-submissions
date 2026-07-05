class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        ana2 = {}
        x = 0
        for i in s:
            if i in ana:
                ana[i] = ana[i] + 1

            else:
                ana[i] = x+1

        for i in t:
            if i in ana2:
                ana2[i] = ana2[i] + 1

            else:
                ana2[i] = x+1
        return ana == ana2

        