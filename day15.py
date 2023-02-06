# 이중 연결 리스트 구현하기
# 228p - 6장 응용예제 01
# 난이도 1점
import random


def isStackFull():
    global stack, SIZE, top
    if top >= SIZE - 1:
        return True
    else:
        return False


def isStackEmpty():
    global stack, top
    if top == -1:
        return True
    else:
        return False


def push(data):
    global stack, top
    if isStackFull():
        print('Stack is full')
    top += 1
    stack[top] = data


def pop():
    global stack, top, SIZE
    if isStackEmpty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global stack, SIZE, top
    if isStackEmpty():
        return None
    return stack[top]


SIZE = 7
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    stone_array = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    random.shuffle(stone_array)

    print("Way to candy house: ", end=" ")
    for stone in stone_array:
        push(stone)
        print(stone, "-->", end=" ")
    print("Our home")

    print("Way to home: ", end=" ")
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, "-->", end= " ")
    print("Candy house")
