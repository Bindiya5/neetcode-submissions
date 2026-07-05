class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        s_s = ''.join(s)
        t_s = ''.join(t)
        return (s_s == t_s)
        