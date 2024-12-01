# LINEAR SEARCH
# In Linear Search, we iterate over all the elements of the array
# and check if  the current element is equal to the target element.
# _______________________________________________________

def linear_search(arr, n, item):
    for i in range(0,n):
        if arr[i] == item:
            return i
    return -1

array = [1,3,8,10,40,23,45,15]
target_item = 23
n = len(array)
result = linear_search(array,n, 23)
if result == -1:
    print("The target item is not present in the array")
else:
    print("The target item is present at index: ", linear_search(array, n, 23))