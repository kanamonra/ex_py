# 이중 연결 리스트 구현하기
# 230p 6장 응용예제 02
# 난이도 3점
# used separate characters one by one


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


SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    exam_array = ['진달래꽃', '나 보기가 역겨워', '가실 때에는', '말없이 고이 보내드리오리다']
    # letter = [x for x in exam_array]

    print("------- 원본 -------")
    for letter in exam_array:
        push(letter)
        print(letter, "\n", end="")
    print()

    print("------- 거꾸로 처리된 결과 -------")
    while True:
        letter = pop()
        if letter == None:
            break
        miniStack = [None for _ in range(len(letter))]
        miniTop = -1
        for ch in letter:
            miniTop += 1
            miniStack[miniTop] = ch

        while True:
            if miniTop == -1:
                break

            ch = miniStack[miniTop]
            miniTop -= 1
            print(ch, end="")

