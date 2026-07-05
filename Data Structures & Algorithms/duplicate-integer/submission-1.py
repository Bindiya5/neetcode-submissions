class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:



#-----------First approach: TC, SC - O(n) --------------

        # a = set(nums)
        # a = list(a)

        # if len(nums) == len(a):
        #     return False
        # else:
        #     return True

    #-----------second approach: TC, SC - O(n) --------------

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

         