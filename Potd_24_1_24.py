'''
You are given an undirected graph of N nodes (numbered from 0 to N-1) and M edges. Return 1 if the graph is a tree, else return 0.

Note: The input graph can have self-loops and multiple edges.

Example 1:
Input:
N = 4, M = 3
G = [[0, 1], [1, 2], [1, 3]]
Output: 
1
Explanation: 
Every node is reachable and the graph has no loops, so it is a tree.

Example 2:
Input:
N = 4, M = 3
G = [[0, 1], [1, 2], [2, 0]]
Output: 
0
Explanation: 
3 is not connected to any node and there is a loop 0->1->2->0, so it is not a tree.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isTree() which takes the integer N (the number nodes in the input graph) and the edges representing the graph as input parameters and returns 1 if the input graph is a tree, else 0.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 2*10^5
0 <= M <= 2*10^5
'''

#User function Template for python3

class Solution:
    def isTree(self, n, m, edges):
        adj_list = {i: [] for i in range(n)}
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n

        def isCyclic(node, parent):
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    if isCyclic(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        def isConnected():
            return all(visited)

        # Check for cycles in the graph
        if isCyclic(0, -1):
            return 0

        # Check if the graph is connected
        if not isConnected():
            return 0

        # Check if the number of edges is equal to (number of nodes - 1)
        return 1 if m == n - 1 else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
# } Driver Code Ends