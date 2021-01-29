# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    for index, item in enumerate(range(elements)):
        #print('index', index, 'item', item)
        if not arrA:
            merged_arr[index] = arrB.pop(0)
        elif not arrB:
            merged_arr[index] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[index] = arrA.pop(0)
        else:
            merged_arr[index] = arrB.pop(0)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
##    mid = len(arr)//2
##
##    if not mid:
##        return arr
##
##    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    try:
        arr[1]
        mid = len(arr)//2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    except IndexError: # len(arr) = 1
        return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
