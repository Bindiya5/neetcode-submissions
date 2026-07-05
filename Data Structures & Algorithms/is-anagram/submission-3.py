class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #------Approach 1 : TC - O(nlogn) , SC - O(n)--------

        # return sorted(s) == sorted(t)

        #--------Second approach --------------------------

        # Time Complexity: 𝑂(𝑛), where 𝑛 is the length of the input strings 
        # if they are the same length. If they are different, the complexity is 𝑂(1)
        # Space Complexity: 𝑂(𝑛), where 𝑛 is the length of the input strings. O(1) if lenths are same


        # The get() function in a dictionary allows you to retrieve 
        # the value for a given key. If the key does not exist in the
        #  dictionary, get() returns a default value, which you can 
        #  specify. This prevents the code from raising a KeyError if 
        #  the key is not found in the dictionary.

        if len(s) != len(t):
            return False

        cS , cT = {} , {}

        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0)
            cT[t[i]] = 1 + cT.get(t[i], 0)

        return cS == cT



        