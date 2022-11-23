# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")

def cmp(a,b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

# must be in-place sort
def merge_sort(arr,cmp):
    if len(arr) > 1:
        # Find the mid of the list or array
        # Take the floor of it to ensure integer result
        mid = len(arr) // 2
        # Left represents first half
        left = arr[:mid]
        # Right represents second half
        right = arr[mid:]
        # Sort first half
        merge_sort(left,cmp)
        # Sort second half
        merge_sort(right,cmp)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if (cmp(left[i],right[j]) == -1) or (cmp(left[i],right[j]) == 0):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Check for remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
    pass

# must be in-place sort
def quick_sort(arr,cmp):
    pass
