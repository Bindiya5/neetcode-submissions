class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        a = set(nums)
        a = list(a)

        if len(nums) == len(a):
            return False
        else:
            return True


         