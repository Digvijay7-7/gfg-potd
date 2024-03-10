'''
Given an array of strings arr[] of length n representing non-negative integers, arrange them in a manner, such that, after concatanating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Example 1:
Input: 
n = 5
arr[] =  {"3", "30", "34", "5", "9"}
Output: "9534330"
Explanation: 
Given numbers are  {"3", "30", "34", "5", "9"}, 
the arrangement "9534330" gives the largest value.

Example 2:
Input: 
n = 4
arr[] =  {"54", "546", "548", "60"}
Output: "6054854654"
Explanation: 
Given numbers are {"54", "546", "548", "60"}, the 
arrangement "6054854654" gives the largest value.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printLargest() which takes the array of strings arr[] as a parameter and returns a string denoting the answer.

Expected Time Complexity: O(n*log(n) ).
Expected Auxiliary Space: O(n).
'''

#User function Template for python3
from functools import cmp_to_key

class Solution:
    def printLargest(self, n, arr):
        # Custom comparator function for sorting strings
        def compare(x, y):
            # Concatenate x and y
            xy = x + y
            yx = y + x
            # Compare xy and yx
            if xy > yx:
                return -1
            elif xy < yx:
                return 1
            else:
                return 0
            '''
            This function concatenates x and y in two different orders: xy (x followed by y) and yx (y followed by x). 
            Then, it compares these concatenated strings. If xy is greater than yx, it returns -1 indicating that x should come before y in the sorted order. 
            If xy is less than yx, it returns 1 indicating that y should come before x. If they are equal, it returns 0.
            '''
        
        # Sort the array using the custom comparator function
        arr.sort(key=cmp_to_key(compare)) 
        '''
         # key parameter of the sort() method ensures that the strings are sorted based on the logic defined in the compare function.         
        '''
        # Concatenate the sorted array elements to form the largest number
        largest_number = ''.join(arr)
        
        return largest_number


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends