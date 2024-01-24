'''
There are a total of n tasks you have to pick, labelled from 0 to n-1. Some tasks may have prerequisite tasks, for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]
Given the total number of n tasks and a list of prerequisite pairs of size m. Find a ordering of tasks you should pick to finish all tasks.
Note: There may be multiple correct orders, you just need to return any one of them. If it is impossible to finish all tasks, return an empty array. Driver code will print "No Ordering Possible", on returning an empty array. Returning any correct order will give the output as 1, whereas any invalid order will give the output 0. 

Example 1:
Input:
n = 2, m = 1
prerequisites = {{1, 0}}
Output:
1
Explanation:
The output 1 denotes that the order is valid. So, if you have, implemented your function correctly, then output would be 1 for all test cases. One possible order is [0, 1].

Example 2:
Input:
n = 4, m = 4
prerequisites = {{1, 0},
               {2, 0},
               {3, 1},
               {3, 2}}
Output:
1
Explanation:
There are a total of 4 tasks to pick. To pick task 3 you should have finished both tasks 1 and 2. Both tasks 1 and 2 should be pick after you finished task 0. So one correct task order is [0, 1, 2, 3]. Another correct ordering is [0, 2, 1, 3]. Returning any of these order will result in an output of 1.
Your Task:
The task is to complete the function findOrder() which takes two integers n, and m and a list of lists of size m*2 denoting the prerequisite pairs as input and returns any correct order to finish all the tasks. Return an empty array if it's impossible to finish all tasks.

Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
'''

#User function Template for python3

from collections import defaultdict, deque
class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        in_degree = [0] * n
        graph = defaultdict(list)

    # Build in-degree and adjacency list
        for pair in prerequisites:
            in_degree[pair[0]] += 1
            graph[pair[1]].append(pair[0])

    # Initialize a queue for topological sorting
        queue = deque()

    # Add nodes with in-degree 0 to the queue
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

    # Initialize result order
        order = []

    # Perform topological sorting
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # Check if all tasks have been included in the order
        if len(order) == n:
            return order
        else:
            return []


# #User function Template for python3

# from collections import defaultdict
# class Solution:
#     def findOrder(self, N, m, P):
#         graph = defaultdict(list)
#         for a, b in P: graph[a].append(b)
#         res, visited = [], [0] * N
#         def DFS(i):
#             if visited[i]: return visited[i] == 1
#             visited[i] = -1
#             if any(not DFS(node) for node in graph[i]): return False
#             visited[i] = 1
#             res.append(i)
#             return True
#         return all(DFS(node) for node in range(N)) and res or []



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends