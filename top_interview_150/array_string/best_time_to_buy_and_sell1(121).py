"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
# 1st solution
# def maxProfit(prices):
#     min = prices[0]
#     profit = 0
#     for i in range(1, len(prices)):
#         if min > prices[i-1]:
#             min = prices[i-1]
#         if prices[i] - min > profit:
#             profit = prices[i] - min
#     return profit

# 2nd solution
def maxProfit(prices):
    left = 0
    right = 1
    maxP = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            maxP = max(maxP, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return maxP




prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))