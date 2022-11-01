#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(wordList[0])    #m is the length of a word in wordlist
        
        wordList = set(wordList)    #Initialize wordList as a set of wordList
        
        wordList.add(beginWord) #Add the beginWord into the wordList
        
        adj = defaultdict(list) #Initialize adjacency matrix as a list 
        for word in wordList:   #For every word in wordList
            for i in range(m):  #Continue till m
                s = word[:i]+ "_" +word[i+1:]   #Maniplate the word string by adding special character "_" at eveery index and add it to the adjacency matrux which ever satisfies
                adj[s].append(word) #Append the corresponding word into the adjacency matrix
                
        q = deque() #Initialize q using deque
        q.append(beginWord) #Append the beignWord to the q
        visited = set() #Initialize visited as a set which tracks the visited words
        dist = 0    #Initialize dist as 0
        visited.add(beginWord)  #Add the beginWord into the visited set
        while q:    #Continue till the q is empty
            dist+=1 #Incerement dist by 1
            size = len(q)   #size is the length of the q
            
            for _ in range(size):   #Continue till the size
                curr = q.popleft()  #Pop the first element in the q and store it in curr
                for i in range(m):  #Continue till m
                    s = curr[:i]+ "_" +curr[i+1:]    #Maniplate the curr string by adding special character "_" at eveery index
                    for nextWord in adj[s]: #For the words in adj 
                        if nextWord not in visited: #If the nextWord is not in visited set then add it to the visited set and append it to the q
                            visited.add(nextWord)
                            q.append(nextWord)
                            if nextWord == endWord: #If the nextWord is equal to endWord return dist+1
                                return dist+1
                            
        return 0    #If nothing is found return 0