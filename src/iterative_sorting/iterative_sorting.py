# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        smallest_value = arr[cur_index]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)        
        for index, item in enumerate(arr[cur_index:]):
            if item < smallest_value:
                smallest_value = item
                smallest_index = index + cur_index

        # TO-DO: swap
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = smallest_value
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = False
    for i in range(0, len(arr) - 1):
        item = arr[i]
    #for index, item in enumerate(arr):
        if item > arr[i + 1]:
            arr[i] = arr[i + 1]
            arr[i + 1] = item
            swapped = True

    if not swapped:
        return arr
    else:
        return bubble_sort(arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if maximum > 0:
        counts = [0] * maximum
    else:
        counts = []
    
    for item in arr:
        if item < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        if item + 1 > len(counts):
            extend_count = item + 1 - len(counts)
            counts = counts + [0] * extend_count
        counts[item] += 1

    arr = []
    
    for index, item in enumerate(counts):
        if item:
            arr = arr + [index] * item
    
    return arr
