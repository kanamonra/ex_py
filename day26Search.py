# Interval search -> Binary search
# more fast for finding non exist data

def binary_search(arr, find_data):
    pos = -1
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == arr[mid]:
            return mid
        elif find_data > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


data_array = [2, 5, 6, 12, 34, 45, 65, 91, 99, 120, 142, 162, 234]

findData = 99

print('Array -->', data_array)
position = binary_search(data_array, findData)
if position == -1:
    print("Not found...", findData)
else:
    print(findData, 'is', position, "th place in data")
