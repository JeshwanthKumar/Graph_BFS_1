# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Time_Complexity: o(n)
#Space_Complexity: O(n)



class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)     #Initialize adjacency matrix as a list
        q = deque() #Initialize q using deque
        q.append(root)  #Appenmd the root into the q
        visited = set() #Initialize visited as a set
        while q:    #Continue till the q is empty
            curr = q.popleft()  #Pop the first element in q and store it in curr
            if curr.left:   #If there is left child
                adj[curr.left].append(curr) #Append the curr as value to curr.left in the adjacency matrix
                adj[curr].append(curr.left) #Append the curr.left as value to curr in the adjacency matrix
                q.append(curr.left) #Append the curr.left to the q
            if curr.right:  #If there is right child
                adj[curr.right].append(curr)     #Append the curr as value to curr.right in the adjacency matrix
                adj[curr].append(curr.right)    #Append the curr.right as value to curr in the adjacency matrix
                q.append(curr.right)    #Append the curr.right to the q
                

        q.append(target)    #Appedn the target to the q
        
        while q and k > 0:  #Continue till the q is empty and k is greater than 0
            size = len(q)   #size is the length of q
            
            for _ in range(size):   #Conitnue till the size
                curr = q.popleft()  #Pop the first element in the q
                visited.add(curr)   #Add the curr to visited
                for neigh in adj[curr]: #FOr every neighbors in the adjacency matrix for curr
                    if neigh not in visited:    #If the neigh is not in visited
                        q.append(neigh) #Append neigh to the q
                    
            k -= 1  #Decrement k by 1
        result = [] #Initialize result as an empty array
        for node in q:  #For all the nodes in q
            result.append(node.val)    #Append the value of those node into result array
            
        return result   #Return result
        