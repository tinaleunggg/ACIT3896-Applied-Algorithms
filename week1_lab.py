def linear_search(needle, haystack):
    counter = 0
    for n in haystack:
        if n == needle:
            return counter
        else:
            counter += 1
    return None

def binary_search(needle, haystack):
    min = 0
    max = len(haystack) - 1
    mid = len(haystack) // 2
    while max >= min:
        mid = (max + min) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] > needle:
            max = mid -1 
        elif haystack[mid] < needle:
            min = mid + 1
    return None
            
def linear_search_multi(needle, haystack):
    output = []
    counter = 0
    for n in haystack:
        if n == needle:
            output.append(counter)
            counter += 1
        else:
            counter += 1
    return output

def binary_search_multi(needle, haystack):
    min = 0
    max = len(haystack) - 1
    mid = len(haystack) // 2
    output = []
    while max >= min:
        mid = (max + min) // 2
        if haystack[mid] == needle:
            output.append(mid)
        elif haystack[mid] > needle:
            max = mid -1 
        elif haystack[mid] < needle:
            min = mid + 1
    return None
