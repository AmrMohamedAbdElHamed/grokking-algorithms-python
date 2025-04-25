def recursive_binary_search(given_list , target, low = 0, high=None) :
    if high == None:
        high =len(given_list)-1
    mid = (low+high)//2
    mid_item = given_list[(low+high)//2]
    if target == mid_item:
        return mid
    elif target > mid_item:
        low= mid
        return recursive_binary_search(given_list, target,low,high)
    elif target < mid_item:
        high= mid
        return recursive_binary_search(given_list, target,low,high)
raw_input = input("Enter a sorted list of numbers: ")
given_list = list(map(int, raw_input.strip().split()))
target = int(input("Enter the number to search for: "))
print(recursive_binary_search(given_list,target))