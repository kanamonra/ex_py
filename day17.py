# 큐 7장
# 272p 응용예제 02
# 난이도 3점


def isQueueFull():
    global SIZE, front, rear
    if rear == SIZE-1:
        return True
    else:
        return False


def isQueueEmpty():
    global SIZE, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Stack is full')
        return
    rear += 1
    queue[rear] = data


def de_queue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for x in range(front+1, rear+1):
        queue[x-1] = queue[x]
        queue[x] = None
    front = -1
    rear -= 1

    return data


def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    return queue[front+1]


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":

    en_queue('Fill')
    en_queue('Mike')
    en_queue('Charlie')
    en_queue('Charly')
    en_queue('Ethan')

    print('Current waiting line: ', queue)

    for _ in range(rear+1):
        print(de_queue(), 'has entered the restaurant')
        print('Current waiting line: ', queue)

    print('Restaurant is closed')