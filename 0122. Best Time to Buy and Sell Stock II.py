'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## http://blog.csdn.net/nomasp/article/details/50829772
        '''
        其实换一种思路，（7 - 4) + (8 - 7) + (8 - 2)
        区别在于，直接将后一个数减前一个数就好了呀，只不过如果后一个数比前一个数小的话就不考虑而已。
        '''
        
        
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff >0:
                profit +=diff
        return profit