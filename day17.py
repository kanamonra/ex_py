# 큐 7장
# 272p 응용예제 02
# 난이도 3점


def isQueueFull():
    global SIZE, front, rear
    if (rear + 1) % SIZE == front:
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
    rear = (rear + 1) % SIZE
    queue[rear] = data


def de_queue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    return queue[(front + 1) % SIZE]


def cal_time():
    global SIZE, queue, front, rear
    time_sum = 0
    for i in range((front + 1) % SIZE, (rear + 1) % SIZE):
        time_sum += queue[i][1]
        return time_sum


SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":

    waiting_time = [('Usage', 9), ('Break down', 3), ('Return', 4), ('Return', 4), ('Break down', 3)]

    for time in waiting_time:
        print('Apparently your waiting time is ', cal_time())

        print('Current waiting line: ', queue)
        en_queue(time)
        print()

    print('Updated waiting line: ', queue)
    print('Program ends...')
