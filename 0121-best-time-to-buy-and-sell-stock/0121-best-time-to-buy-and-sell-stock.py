class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buying and selling on which days will allow you to make maximum profit = largest difference between
        # two values
            # buy on minimum day and sell on maximum day
        # matching - array problem - at least O(n) bc need to see all values to make a determination of what 
        # max profit would be 

        # pseudo 
        # go through all prices 
        # keep track of a minimum variable bc thats when you would buy the stock and update it if you find a lower prices
        # if you find a higher number than minimum, see if the profit would be greater and update maxprofit
         

        minimum = float(inf)
        maximumProfit = float(-inf)
        for price in prices:
            if price < minimum: # buy
                minimum = price
            elif price > minimum: # sell 
                maximumProfit = max(maximumProfit, price-minimum)
        if maximumProfit != float(-inf):
            return maximumProfit
        else:
            return 0


        # 