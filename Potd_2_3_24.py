'''
Given an array of n integers. Find the first element that occurs atleast k number of times. If no such element exists in the array, then expect the answer to be -1.

Example 1:
Input :
n = 7, k = 2
a[] = {1, 7, 4, 3, 4, 8, 7}
Output :
4
Explanation :
Both 7 and 4 occur 2 times. But 4 is first that occurs twice.
As at index = 4, 4 has occurred twice whereas 7 appeared twice
at index 6.

Example 2:
Input :
n = 10, k = 3
a[] = {3, 1, 3, 4, 5, 1, 3, 3, 5, 4}
Output :
3
Explanation :
Here, 3 is the only number that appeared atleast 3 times in the array.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function firstElementKTime() which takes the array a[], its size n, and an integer k as input arguments and returns the required answer. If the answer is not present in the array, return -1.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
'''

#User function Template for python3
class Solution:
    def firstElementKTime(self, n, k, a):
        counts = {}  # Use a dictionary to track element counts
        first_index = {}  # Store first index for elements appearing k times
        
        for i in range(n):
            counts[a[i]] = counts.get(a[i], 0) + 1
            if counts[a[i]] == k:
                if a[i] not in first_index:  # Check if first occurrence of k
                    first_index[a[i]] = i
        
        # Find minimum first index among elements appearing k times
        min_index = min(first_index.values()) if first_index else -1
        return a[min_index] if min_index != -1 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))
        T -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends