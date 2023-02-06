# 이중 연결 리스트 구현하기
# 199p - 5장 응용예제 02
# 난이도 2점

class Node:
    def __init__(self):
        self.plink = None  # first
        self.data = None
        self.nlink = None  # at end


def print_node(start):
    current = start
    if current.nlink == None:
        return
    print('정방향 -->', end=' ')
    print(current.data, end=" ")
    # end link

    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()
    print('역방향 -->', end=' ')
    print(current.data, end=" ")
    # first link
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')


head, current, pre = None, None, None
data_array = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.nlink = node
        node.plink = pre

    print_node(head)
