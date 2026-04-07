def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]

def selection_sort(seq):
    cur = 0
    while cur < (len(seq) -1):
        smallest = seq[cur]
        smallest_index = cur

        for i in range(cur, len(seq)):
            if seq[i] < smallest:
                smallest = seq[i]
                smallest_index = i
        # swap 
        temp = seq[cur] 
        seq[cur] = seq[smallest_index]
        seq[smallest_index] = temp

        cur += 1

def insertion_sort(seq):
    cur = 1
    while cur < len(seq):
        for i in range(cur, 0, -1):
            if seq[i] < seq[i -1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
            else:
                break
        cur += 1
