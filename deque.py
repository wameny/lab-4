from collections import deque

queue = deque([1, 4, 6, 9, 0, 2])

def append_right(item):
    queue.append(item)
    return queue

def append_left(item):
    queue.appendleft(item)
    return queue

def pop_right():
    if queue:
        queue.pop()
        return queue
    return None

def pop_left():
    if queue:
        queue.popleft()
        return queue
    return None

def peek_right():
    if queue:
        return queue[-1]
    return None

def peek_left():
    if queue:
        return queue[0]
    return None

print(append_right(10))
print(append_left(99))

print(pop_right())
print(pop_left())

print(peek_right())
print(peek_left())