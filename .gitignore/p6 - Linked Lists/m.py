class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def list_to_linked(alist):
    if not alist: return None

    head = ListNode(alist[0]) #initialize the head node with the first value of the list
    current = head

    for num in alist[1:]:
        current.next = ListNode(num) #linkes curent node eg head node, to ListNode(num) ie the new node that has been created.or the node after the head node for instance
        current = current.next # makes the current node the second node. the cycle continues. 
    return head #return head node of linked list

linked_list = list_to_linked([1,2,3,3,4,5,3,5,3,5,6,7,8]) #make the linked list. This is the head node btw. This list is an instance of the ListNode class. 

def Reverse_a_Linked_List(head): #To reverse a linked list, you need to rearrange the next pointers of the nodes. THIS IS A 2 POINTER PROBLEM
    prev = None
    current = head #current doesnt hold the alist head node, but a reference. In essence we are not directly manipulation the inputted linked list in a way. 

    while current: #while current is not none 
        next_node = current.next #we preseerve the connection between 2 nodes because we are going to use current and change its direction using prev
        current.next = prev #make current node point to the prev. So if current is 1, we are making it point at None. 
        prev = current #what we are doing is moving prev to the position of current, for this example we moved prev to the position of 1 -> None. We need to understanding that there are 2 components to manipulation linked lists: pointing and moving, which are different actions. 
        current = next_node #point to the next node. 
    return prev    

def print_a_linked_list(alist):#To use the output of the print function we have to make the function return the print #remember we cant just do alist.val because we have to move next. 
    while alist:
        print(f'{alist.val} -> ', end = "") # End specifies what should be at the end of the printed string. But default it goes to a new line. 
        '''print("Hello", end="")
        print("World") is HelloWorld'''
        alist = alist.next
    print("None")

#print_a_linked_list(Reverse_a_Linked_List(linked_list))

def remove_dupes(head): #not just a sorted list, any list. 
    
    prev = None
    current = head
    seen = set() #Checking if an item is in a set is on average O(1) time complexity, while checking if an item is in a list is O(n) time complexity
    while current:
        if current.val not in seen: 
            seen.add(current.val)
            prev = current            
        else:
            if prev: prev.next = current.next #This needs to exist outside the if statements, because this is essentially the main iterator that goes over each of the nodes and will progress through the list regardless of the if statements. 
        current = current.next
    return head

print_a_linked_list(remove_dupes(linked_list))

def find_middle_of_linked_list(head):

    slow = head
    fast = head

    while fast and fast.next: #because of the lengths of input lists (odd or even) and for traversal problems jst check both fast and fast.next.
        
        slow = slow.next
        fast = fast.next.next #instead of moving fast to the next element, move fast to the element after the next. while the slow pointer moves 1 element at a time. by the time fast pointer completes the list, slow pointer will make it half way through the list. then return slow pointer. 
    
    return slow

def merge_k_sorted_linked_list():
    