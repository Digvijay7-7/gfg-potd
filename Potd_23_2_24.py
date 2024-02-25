'''
In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices. 

Given an array price of size n, find out the maximum profit that a share trader could have made.

Example 1:
Input:
n = 6
prices[] = {10,22,5,75,65,80}
Output:
87
Explanation:
Trader earns 87 as sum of 12, 75 Buy at 10, sell at 22, Buy at 5 and sell at 80.

Example 2:
Input:
n = 7
prices[] = {2,30,15,10,8,25,80}
Output:
100
Explanation:
Trader earns 100 as sum of 28 and 72 Buy at price 2, sell at 30, Buy at 8 and sell at 80,
Your Task:

Complete the function maxProfit() which takes an integer array price as the only argument and returns an integer, representing the maximum profit, if only two transactions are allowed.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:

1 <= n <= 10^5
1 <= price[i] <= 10^5
'''
from typing import List

class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n < 2:
            return 0
        
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        
        for p in price:
            buy1 = max(buy1, -p)                
            sell1 = max(sell1, buy1 + p)        
            buy2 = max(buy2, sell1 - p)        
            sell2 = max(sell2, buy2 + p)       
            
        return sell2

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):        
        n = int(input())        
        price=IntArray().Input(n)        
        obj = Solution()
        res = obj.maxProfit(n, price)        
        print(res)
        
# } Driver Code Ends