# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
   for index, item in enumerate(arr):
      if item == target:
         return index

   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
   if len(arr) == 0:
      return -1 # array empty
    
   low = 0
   high = len(arr)-1
   middle = (low + high) // 2
   middle_value = arr[middle]

   while True:
      if middle_value == target:
         return middle
      elif high - low == 1:
         return -1 # not found
      elif middle_value < target:
         low = middle
         middle = (low + high) // 2
         middle_value = arr[middle]
      elif middle_value > target:
         high = middle
         middle = (low + high) // 2
         middle_value = arr[middle]


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

   if len(arr) == 0:
      return -1 # array empty

   middle = (low+high)//2
   middle_value = arr[middle]

   if middle_value == target:
      return middle
   elif high - low == 1:
      return -1 # not found
   elif middle_value < target:
      return binary_search_recursive(arr, target, middle, high)
   elif middle_value > target:
      return binary_search_recursive(arr, target, low, middle)
      
