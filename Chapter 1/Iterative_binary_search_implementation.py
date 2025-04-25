def iterative_binary_search_implementation(given_list,target):
    low = 0
    high = len(given_list)-1 
    while low <= high:
        mid = (low+high)//2
        mid_item = given_list[mid]
        if mid_item == target:
            return mid
        elif mid_item > target:
            high = mid-1
        elif mid_item < target:
            low = mid+1

print(iterative_binary_search_implementation([10,20,30,40,50],10))