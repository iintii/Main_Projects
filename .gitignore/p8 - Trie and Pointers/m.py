class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0 #Each node ie each letter will have its own prefix count. 
class Trie: #using self for the methods because they are inside a class and need to refer to themselves to distinguish themselves. not needed if the fnx was outside the class. 
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):#root node and subsequent nodes can contain as many letters as needed, if the letters dont match. 
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end_of_word

    def search(self, word): #search function is implimented on a single word. we use a for loop to feed single words from a list of words into search. So dw about it not being a list. 
        #if not word: return "" wheher the words are valid check is done in the main call, not here. 

        node = self.root #we start at the root node. 
        for char in word:
            if char not in node.children:
                return False #meaning that the first letter doesnt exist in the dict, ie the word doesnt exist in the dict. 
            node = node.children[char] #progress through the hierarchy
        node.is_end_of_word == True #if a word is in dict, it will return true. 
    
    def countWordsStartingWith(self, prefix):

        node = self.root
        count = 0

        for char in prefix:
            if prefix[0] not in node.children:  return 0 
            node = node.children[char] #when the dictionary is created, that is when a count is kept for each time a letter passes through a node
        return node.prefix_count #all we do is update the node to the last char in prefix, the return statement returns the count at the last char in the prefix. 

    def delete(self, word):
        node = self.root
        while node.is_end_of_word == False:
            for char in word:
                if char not in node.children: print ("Word not found")
                

                
                




            
