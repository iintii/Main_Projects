def merge_sort(alist):

    if len(alist) <= 1: return alist

    midpoint = len(alist) // 2
    left, right = alist[:midpoint], alist[midpoint:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_list = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted_list.append(left_sorted[i])
            i += 1
        else:
            sorted_list.append(right_sorted[j])
            j += 1
    
    sorted_list.extend(left_sorted[i:])
    sorted_list.extend(right_sorted[j:])

    return sorted_list


#This was a problem shown in class with a divide and conquer soln. 
def max_subarray(alist): #The max subarray prob tries to find the contiguous sublst in a list with the max sum. Meaning which vals in a row will produce the max sum. 
    max_current = alist[0]
    max_global = alist[0]

    for i in range(1, len(alist)): 
        max_current = max(alist[i], alist[i] + max_current) #find the max between the current element or the current element and sum of all the prev elements. since we try to find the sum of continuous elements, if the current num is bigger than the sum of all prev, its beter to start the sum from the current val again. 
        if max_current > max_global:
            max_global = max_current # if the current val is greater than prev max, replace. 
    return max_global

print(max_subarray([-1, 2, 0, -5, 7, 8, -9, 3, 5, 7, 0, -3, 9, -5, -6, 3]))
