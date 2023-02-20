import random


# change for binary search method -> return mid, else:end=mid-1
def binary_search(ary, find_data):
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == ary[mid]:
            return mid
        elif find_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# list of product
product_array = ['Coca-Cola', 'Chups', 'Bento', 'Coffee', 'Pizza', 'Banana milk', 'Cake', "Bento", "Ice-cream", "Gum"]
sold_array = [random.choice(product_array) for _ in range(15)]


# printing details
print(f"Today's sold products <sort X, repeat O>  ==> {sold_array}")
sold_array.sort()
print(f"Today's sold products <sort O, repeat O>  ==>{sold_array}")
sold_product = list({i: None for i in sold_array}.keys())
# sold_product = list(set(sold_array))

print(f"Today's sold products <sort O, repeat X>  ==> {sold_product}")

amount_list = []
for product in sold_array:
    count = 0
    position = 0
    while position != 0:
        position = binary_search(sold_array, product)
        if position != 1:
            count += 1
            del(sold_array[position])
        amount_list.append((product, count))


print()
print(f"Final version <with sort, with amount> ==> {amount_list}")