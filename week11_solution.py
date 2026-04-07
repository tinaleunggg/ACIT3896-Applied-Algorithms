def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)

def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    half = len(seq) // 2
    left = seq[:half]
    right = seq[half:]

    merge_sort(left)
    merge_sort(right)

    output = merge(left, right)

    for i in range(len(seq)):
        seq[i] = output[i]
    

def merge(left, right):
    left_index = 0
    right_index = 0

    output = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            output.append(right[right_index])
            right_index += 1
        else:
            output.append(left[left_index])
            left_index += 1
    
    output.extend(left[left_index:])
    output.extend(right[right_index:])

    return output