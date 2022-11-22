
def binary_search(list, item):
    low = 0
    high = len(list)-1

    count = 1

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        
        print(count)
        count += 1

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = list(range(0, 1000000, 1))

# print(my_list)
print(binary_search(my_list, 0))

# 1000 = 2^10
# 1000000 = 2^20
# 1000000000 = 2^30