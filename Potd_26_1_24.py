'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here. 

Example 1:

Input:
N = 3, W = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total weight becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 
Example 2:

Input:
N = 2, W = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size N and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)

Constraints:
1 <= N <= 10^5
1 <= W <= 10^9
1 <= valuei, weighti <= 10^4
'''

#User function Template for python3

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # Calculating the value-to-weight ratio for each item.
        for item in arr:
            item.vw_ratio = item.value / item.weight

        # Sorting the items based on the value-to-weight ratio in descending order.
        arr.sort(key=lambda x: x.vw_ratio, reverse=True)

        total_value = 0  # Total value in the knapsack
        current_weight = 0  # Current weight in the knapsack

        # Loop through each item and add to the knapsack until it's full.
        for item in arr:
            if current_weight + item.weight <= W:
                total_value += item.value
                current_weight += item.weight
            else:
                # If the item cannot be added completely, add a fraction of it.
                remaining_capacity = W - current_weight
                fraction = remaining_capacity / item.weight
                total_value += item.value * fraction
                break

        return total_value

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends