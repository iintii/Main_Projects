def frequency_counter(alist):
    hm = {}
    for val in alist:
        #hm[val] = 1 #This resets the counter so no
        if val in hm: hm[val] += 1
        else: hm[val] = 1

    return hm

print(frequency_counter([1,2,1,3,4,4,4,5,6,5,5]))

def two_sum(alist, target):
    hm = {}
    for i, num in enumerate(alist):
        val = target - num
        if val in hm: return [hm[val], i]
        hm[num] = i
    return None

def is_anagrams(word1, word2):
    #user input
    if not isinstance(word1, str) or not isinstance(word2, str): raise ValueError("Both inputs must be strings")
    if word1 == '' and word2 == '': return word1 == word2
    if word1 is None or word2 is None: return None
    hmw1, hmw2 = {}, {}

    for char in word1:
        if char in hmw1: hmw1[char] += 1
        else: hmw1[char] = 1
    for char in word2:
        if char in hmw2: hmw2[char] += 1
        else: hmw2[char] = 1

    return hmw1 == hmw2

print(is_anagrams('listen', 'silent'))

def key_value_swap(adict):
    if not isinstance(adict, dict): raise ValueError("Input needs to be a dictionary")

    swapped_d = {}#using a new dicitionary because if we modify the dict while iterating over it at the same time, it will cause run time errors. 
    for key, val in adict.items():
        swapped_d[val] = key
    return swapped_d

print(key_value_swap({"a": 1, "b": 2, "c": 3}))

