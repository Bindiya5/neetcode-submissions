class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #-----------Approach 1 : TC- O(n^2) , SC - O(1) ---------------
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        #--------------Approach 2---------------------

        d = {value: index for index, value in enumerate(nums)}

        for i in range(len(nums)):
            k = target - nums[i]
            if ((k in d) and i != d[k]):
                return [i, d[k]]
        