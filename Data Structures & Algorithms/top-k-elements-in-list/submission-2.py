class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #---------TC: O(n log n), SC: O(n) ----------------
        
        # from collections import Counter

        # numsDict = Counter(nums)
        # numsDict = dict(numsDict)

        # sorted_dict = dict(sorted(numsDict.items(), key=lambda item: item[1]))

        # keys = list(sorted_dict.keys())

        # x = keys[-k:]
        # return x

        #---------------------------------------

        count = {}
        freq = [ [] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)

        for n,c in count.items():
            freq[c].append(n)

        res =[]
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]


        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     print("count[n] = " + str(count))
        # for n, c in count.items():
        #     freq[c].append(n)
        #     print("freq=" + str(freq))

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         print("res=" + str(res))
        #         if len(res) == k:
        #             return res



    