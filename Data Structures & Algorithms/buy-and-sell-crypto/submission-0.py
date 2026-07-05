class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        p = 0
        for r in range(l+1,len(prices)):
            print(prices[r],prices[l])
            if prices[r] > prices[l]:
                p = max(p,(prices[r] - prices[l]))
                print("profit = " + str(p))
            else:
                l=r
        return p

        