class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter

        numsDict = Counter(nums)
        numsDict = dict(numsDict)
        print(numsDict)

        sorted_dict = dict(sorted(numsDict.items(), key=lambda item: item[1]))

        keys = list(sorted_dict.keys())

        x = keys[-k:]
        return x

    