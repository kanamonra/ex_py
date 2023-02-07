# 큐 8장
# 309p 응용예제 01
# 난이도 2점
# count how many product has overlap
import random


class tree_node():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


memory = []

item_array = ['Banana milk', 'Coffee', 'Chupa chups', 'Fast food', 'Water', 'Cola', 'Onigiri']
selled_array = [random.choice(item_array) for _ in range(10)]

print("Today's sells(overlap)", selled_array)

node = tree_node()
node.data = selled_array[0]
root = node
memory.append(node)

for name in selled_array[1:]:
    node = tree_node()
    node.data = name
    current = root
    while True:
        if name == current.data:
            pro_count = selled_array.count(name)
            break
        elif name < current.data:
            if current.left == None:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                memory.append(node)
                break
            current = current.right


print('Binary tree data management has done!')
print("The most repeated product number: ", pro_count)

def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


print("Today's sells(non-overlap)", end=' ')

preorder(root)
