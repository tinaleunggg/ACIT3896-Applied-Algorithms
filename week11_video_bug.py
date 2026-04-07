def magical_search(needle, haystack):
	if len(haystack) == 0:
		return None
	
	halfway_index = len(haystack) // 2
	
	if haystack[halfway_index] == needle:
		return halfway_index
	elif haystack[halfway_index] > needle:
		first_half = haystack[:halfway_index]
		return magical_search(needle, first_half)
	else:
		second_half = haystack[halfway_index +1:]
		return magical_search(needle, second_half)
	

haystack = [1,2,3,4,5,6,7,8,9]
print(magical_search(9, haystack))
