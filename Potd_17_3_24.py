'''
Given two linked list head1 and head2 with distinct elements, determine the count of all distinct pairs from both lists whose sum is equal to the given value x.

Note: A valid pair would be in the form (x, y) where x is from first linked list and y is from second linked list.

Example 1:
Input:
head1 = 1->2->3->4->5->6
head2 = 11->12->13
x = 15
Output: 3
Explanation: There are total 3 pairs whose sum is 15 : (4,11) , (3,12) and (2,13)

Example 2:
Input:
head1 = 7->5->1->3
head2 = 3->5->2->8
x = 10
Output: 2
Explanation: There are total 2 pairs whose sum is 10 : (7,3) and (5,5)
Your Task:
You only need to implement the given function countPairs() that take two linked list head1 and head2 and return the count of distinct pairs whose sum is equal to x.

Expected Time Complexity: O(length(head1)+lenght(head2)).
Expected Auxiliary Space: O(length(head1)) or O(length(head2)).
'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        
# } Driver Code Ends

#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        # Initialize a set to store elements of one linked list
        seen = set()
        count = 0
        
        # Traverse the first linked list and add elements to the set
        current = head1
        while current:
            seen.add(current.data)
            current = current.next
        
        # Traverse the second linked list and check if the complement exists in the set
        current = head2
        while current:
            complement = x - current.data
            if complement in seen:
                count += 1
            current = current.next
        
        return count
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        x=int(input())
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,x))
        
# } Driver Code Ends