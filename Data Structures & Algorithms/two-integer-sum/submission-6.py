class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     k = target - nums[i]
        #     for j in range(i+1, len(nums)):        
        #         if nums[j] == k:
        #             return [i,j]

        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i

        for i in range(len(nums)-1):
            k = target - nums[i]
            if k in hm and hm[k] != i:
                return [i,hm[k]]
        