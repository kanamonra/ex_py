from operator import itemgetter


def make_idx(array, position):
    before_array = []
    idx = 0
    for data in array:
        before_array.append((data[position], idx))
        idx += 1
    # for idx in range(len(array)):
    #     for data in array:
    #         before_array.append(data[position], idx)

    sorted_array = sorted(before_array, key=itemgetter(0))
    return sorted_array


def binary_search(ary, find_data):
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == ary[mid][0]:
            return ary[mid][1]
        elif find_data > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


# list
book_array = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
              ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰'],
              ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
name_idx = []
author_idx = []

# printing details
print('# 책장의 도서 ==>', book_array)
name_idx = make_idx(book_array, 0)
print('# 도서명 색인표 ==>', name_idx)
author_idx = make_idx(book_array, 1)
print('# 작가명 색인표 ==>', author_idx)

find_name = '신곡'
findPos = binary_search(name_idx, find_name)
if findPos != -1:
    print(f"{find_name}의 작가는 {book_array[findPos][1]}입니다.")
else:
    print(f"{find_name} 책은 없습니다.")

find_name = '괴테'
findPos = binary_search(author_idx, find_name)
if findPos != -1:
    print(f"{find_name}의 도서는 {book_array[findPos][0]}입니다.")
else:
    print(f"{find_name} 작가는 없습니다.")
