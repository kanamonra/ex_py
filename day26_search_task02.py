import random

# global
count = 0


def sequance_search(ary, data_in):
    global count
    pos = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == data_in:
            pos = i
            break
    return pos


def binary_search(ary, data_in):
    global count
    start = 0
    end = len(ary) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2
        if data_in == ary[mid]:
            return mid
        elif data_in > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


find_data = 8888


data_array = [random.randint(0, 999999) for _ in range(1000000)]
data_array.insert(random.randint(0, 1000000), find_data)
sorted_array = sorted(data_array)


# printing details
print(f"<Without>  ==> {data_array[0:5]} {data_array[-5:len(data_array)]}")
print(f"<With>  ==> {sorted_array[0:5]} {sorted_array[-5:len(data_array)]}")

pos = binary_search(sorted_array, find_data)
if pos != -1:
    print(f"Binary search count => {count} times")

count = 0
pos = sequance_search(data_array, find_data)
if pos != -1:
    print(f"Sequence search count => {count} times")


