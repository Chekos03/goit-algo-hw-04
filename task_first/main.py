import timeit
import random 
# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr

# Timesort сортування
def timesort(arr):
    return sorted(arr)




def measure(func, arr):
    repeats = 4
    total = timeit.timeit(lambda: func(arr.copy()), number=repeats)
    return total/repeats



def generate_arrays(size):
    arr_random = random.sample(range(size), size)
    arr_sorted = sorted(arr_random)
    arr_reversed = arr_sorted[::-1]
    return arr_random, arr_sorted, arr_reversed


sizez = [1000,2000,5000,10000]
for size in sizez:
    arr_random, arr_sorted, arr_reversed = generate_arrays(size)
    #random
    time_m_random = measure(merge_sort,arr_random)
    time_i_random = measure(insertion_sort,arr_random)
    time_t_random= measure(timesort,arr_random)

    #sorted
    time_m_sorted = measure(merge_sort, arr_sorted)
    time_i_sorted = measure(insertion_sort, arr_sorted)
    time_t_sorted = measure(timesort, arr_sorted)

    #reversed
    time_m_reversed = measure(merge_sort, arr_reversed)
    time_i_reversed = measure(insertion_sort, arr_reversed)
    time_t_reversed = measure(timesort, arr_reversed)

    print(f"-Size {size}")
    print(f"Random: merge = {time_m_random}  insertion = {time_i_random} timsort = {time_t_random}")
    print(f"Sorted: merge = {time_m_sorted}, insertion = {time_i_sorted}, timsort = {time_t_sorted}")
    print(f"Reversed: merge = {time_m_reversed}, insertion = {time_i_reversed}, timsort = {time_t_reversed}")
















