class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize left and right pointers
        # compare first 2 so we initiallize l and r as 0, 1
        l, r = 0, 1

        # default the difference / profit to be ZERO
        max_diff = 0

        # while loop for the right pointer to traverse the list
        while r < len(prices):

            # check if l value is smaller than r
            # calc profit
            # increment l
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_diff = max(max_diff, profit)
            else:
                # either l is bigger or they're equal
                # either way, the "largest" diff has been "explored"
                # so just move l up to r to check for new possibilities of
                # max profit
                l = r
            
            # increment r at the end of while loop block
            r += 1
        
        # return the max profit
        return max_diff


