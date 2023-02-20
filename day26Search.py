# Searching algorithm
def search(array, array_length, input_num):
    for i in range(0, array_length):
        if array[i] == input_num:
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50, 66, 76, 95, 230]
    x = 66
    N = len(arr)

    # Search function call
    result = search(arr, N, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)