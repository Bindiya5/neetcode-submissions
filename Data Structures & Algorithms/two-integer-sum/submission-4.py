class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            print("i = " + str(i))
            k = target - nums[i]
            for j in range(i+1, len(nums)):
                print("nums[i] = " + str(nums[i]))
                print("j = " + str(j))
                print("k = " + str(k))
                
                if nums[j] == k:
                    return [i,j]
        