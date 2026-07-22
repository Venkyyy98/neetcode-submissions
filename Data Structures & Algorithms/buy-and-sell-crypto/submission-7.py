class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        profit = 0
        maxP = 0
        while l<len(prices):
            r = l+1
            while r<len(prices):
                if prices[l]>prices[r]:
                    print("left is bigger",prices[l],prices[r])
                    r +=1
                elif prices[l]<prices[r]:
                    print("right is bigger",prices[l],prices[r])
                    profit = prices[r] - prices[l]
                    maxP = max(maxP, profit)
                    r +=1
                else:
                    print("both are same",prices[l],prices[r])
                    r +=1
            l +=1
        return maxP
                
                    
        