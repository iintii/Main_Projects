class MaxHeap:
    def __init__(self):
        self.heap = [] #constructor so that heap stays initialized regardless of which method is used in
    def maxHeapify(self, i): #heapifying is not the same as sorting, its being put into the order of the binary tree where the parent is largest or smallest after comparing to its child nodes. 
        largest = i #current index
        #positions of left and right child in the array. We treat the array like a binary tree
        left = 2*i + 1 
        right = 2*i + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]: #if the left index is still valid ie less than the len of the array and if the left value in the tree is bigger than its parent, then replace the parent with the left node
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right #replace the current largest index (either the parent or the left index which replaced the parent) with the right index

        if largest != i: #i is the current index tha was at the start of the maxheap function where as largest would be the either the left or right node that replaced the i. 
            self.heap[i] ,self.heap[largest] = self.heap[largest], self.heap[i] #replace current parent index with one of the child node index
            self.maxHeapify(largest) #recursively call function with the index of the node which previously had the largest child node. 
    
    def heapsortmax(self):
        for i in range(len(self.heap)//2-1, -1, -1):
            self.maxHeapify(i) #heapify 1 more time before sorting

        sorted_lst = []
        while len(self.heap) > 0: #stopping condition
            # Step 2: Swap the root (max element) with the last element. So in a max heap, the first element should be the largest
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            # Step 3: Pop the last element (max element) and add to sorted list
            sorted_lst.append(self.heap.pop())
            # Step 4: Heapify the reduced heap
            self.maxHeapify(0)#heapify root, which now should contain a leaf node. maxheapify method will heapify the entire list.

        self.heap = sorted_lst


class MinHeap:
    def __init__(self):
        self.heap = []
    def minHeapify(self, i):
        smallest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)
    
    def heapsortedmin(self):
        for i in range(len(self.heap)//2-1, -1, -1):
            self.minHeapify(i)

        sorted_list = []
        while len(self.heap) > 0:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            sorted_list.append(self.heap.pop())
            self.minHeapify(0)
        
        self.heap = sorted_list
    
if __name__ == "__main__":
    alist = [3,2,4,5,6,2,7,8,9,1]

    maxheap = MaxHeap()
    maxheap.heap = alist.copy()
    """for i in range(len(maxheap.heap)//2-1, -1, -1): #we use a for loop and start with the last node in the "tree" that is not a leaf node. len(maxheap.heap)//2-1 represents that. -1 is not inclusive as the end point ie we want to stop at index 0, so we use -1. and we use -1 to count backwards. remember these are all indices. 
        maxheap.maxHeapify(i)
    print(maxheap.heap)"""

    maxheap.heapsortmax()
    print("Sorted max array is:", maxheap.heap)

    minheap = MinHeap()
    minheap.heap = alist.copy()
    minheap.heapsortedmin()
    print("Sorted min array is:", minheap.heap)

