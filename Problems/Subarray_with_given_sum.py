'''
Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''
i = 0
j = 0
sum = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
s = 21
f = False
while j < n:
    sum += arr[j]
    
    while sum > s:
        sum -= arr[i]
        i+=1
        
    if sum == s:
        f = True
        break
    j+=1
    
if f:
    print("Subarray with sum", s, "found from index", i + 1, "to", j + 1)
else:
    print("No subarray found with the given sum.")

# left = 0
#     right = 0
#     current_sum = 0
    
#     while right < N:
#         current_sum += arr[right]
        
#         while current_sum > S:
#             current_sum -= arr[left]
#             left += 1
        
#         if current_sum == S:
#             return [left + 1, right + 1]  # Adding 1 for 1-based indexing
        
#         right += 1
    
#     return [-1]