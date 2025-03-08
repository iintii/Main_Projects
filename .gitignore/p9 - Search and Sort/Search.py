from Sort import merge_sort

def closest_element_to_target(alist, target): #find closest value to target in a SORTED LIST
    l, r = 0, len(alist) - 1

    while l <= r: #we have created a loop which moves l and r indices but doesnt find the target. thus the loop always exits @ l > r. if the target exists in the list, the loop will always end such that l is always one index higher that target and r is one index less than target. this is becau se the function of the loop is a search ie move l and r closer to target unti the target is found ( but we dont need to find target here)
        m = (l+r) // 2
        if alist[m] < target:   l = m + 1
        else: r = m - 1
    if l >= len(alist): return alist[r] #if the target is greater than all values in the list, l will eventually move out of the index range of the list and we have to return alist[r] because that would be the highest valid value. 
    elif r < 0: return alist[l]
    elif (alist[l] - target) < (target - alist[r]): return alist[l]
    else: return alist[r]

print(closest_element_to_target(merge_sort([2, 1, 80, 45, 100, 79, 234, 163]), 50))
    
def Count_the_Number_of_Occurrences(alist, target): #SINCE THE LIST IS SORTED ALL THE OCCURENCES OF THE NUMBER WILL BE IN A ROW SO WE DONT NEED TO CHECK EACH VALUE, WE ONLY NEED TO FIND THE INDEX OF THE FIRST AND LAST OCCURENCE.
    #return alist.count(target) but this uses O(n) complexity

    def find_left(alist, target):
        l,r = 0, len(alist) - 1
        first_index = -1
        while l <= r:
            m = (l+r)//2
            if alist[m] == target:
                first_index = m
                r = m - 1
            elif alist[m] < target: l = m + 1
            else: r = m - 1
        return first_index
    def find_right(alist, target):
        l,r = 0, len(alist) - 1
        last_index = -1
        while l<=r:
            m = (l+r) // 2
            if alist[m] == target:
                last_index = m
                l = m + 1
            elif alist[m] < target: l = m + 1
            else: r = m - 1
        return last_index
    left_oc, right_oc = find_left(alist, target), find_right(alist, target)
    if left_oc == -1 or right_oc == -1: return 0
    return right_oc - left_oc + 1

print(Count_the_Number_of_Occurrences(merge_sort([3,3,4,5,3,2,4,5,6,7,4,3,1]), 4))

#Bitonic Array - [1, 3, 8, 12, 4, 2], increases to a max height / value then decreases. Sorting then finding max val is O(nlogn) where as using binary search is just O(logn)

def bitonic_max(alist): #insert a bitonic array
    l,r = 0, len(alist) - 1
    while l <= r:
        m = (l+r) // 2
        if m < (len(alist) - 1) and alist[m] > alist[m + 1]: r = m #Important to pay attention to the structure of the bitonic array, after the largest element the numbers decrease in size. if current element bigger than next element, then current element could be the highest number, but the next element is definitely not the highest. so move right pointer to the position of the current m.
        else: l = m + 1 #if current element less than next element, then current element certainl not the highest so no l = m. and highest is in the second half the array. 
    return alist[r] 

print(bitonic_max([[1, 3, 8, 12, 4, 2]]))

def Find_the_First_Element_Greater_Than_or_Equal_to_Target(alist, target):
    l,r = 0, len(alist) - 1
    while l <= r:
        m = (l+r) // 2
        if alist[m] == target or alist[m - 1] == target: return alist[m]
        elif alist[m] < target: l = m + 1
        else: r = m - 1
    return alist[l] if l < len(list) else None #If the target is not in the list, the l index will end up at the index where the target would have been

print(Find_the_First_Element_Greater_Than_or_Equal_to_Target([1, 3, 5, 6], 4))

def Find_an_Element_in_an_Infinite_Sorted_Array(alist, target):
    first, last = 0, 1
    while target > alist[last]: #this is an index search. 
         first = last + 1 # 1 - 2, 3 - 4, 5 - 8, 9 - 16, 10 - 32 etc
         last *= 2
    
    while first <= last:
        m = (first + last) // 2
        if alist[m] == target: return m
        elif alist[m] < target: first = m + 1
        else: last = m - 1
    return -1

def fixed_point_in_array(alist):
    l,r = 0, len(alist) - 1
    while l<=r:
        m = (l+r) // 2
        if alist[m] == m: return m
        elif alist[m] < m: l = m + 1
        else: r = m - 1
    return -1
    
