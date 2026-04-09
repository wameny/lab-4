from collections import deque

queue = deque([1, 4, 6, 9, 0, 2])

def append_right(queue, item):
    queue.append(item)
    return queue

def append_left(queue, item):
    queue.appendleft(item)
    return queue

def pop_right(queue):
    if queue:
        queue.pop()
        return queue
    return None

def pop_left(queue):
    if queue:
        queue.popleft()
        return queue
    return None

def peek_right(queue):
    if queue:
        return queue[-1]
    return None

def peek_left(queue):
    if queue:
        return queue[0]
    return None

print(append_right(queue, 10))
print(append_left(queue, 99))

print(pop_right(queue))
print(pop_left(queue))

print(peek_right(queue))
print(peek_left(queue))