from collections import deque

#1 - highest priority

queue = deque([
    (3, 'homework'),
    (1, 'hospital'),
    (2, 'cooking'),
    (7, 'playing')])

def enqueue(queue, priority, item):
    queue.append((priority, item))
    return queue

def dequeue_high(queue):
    if queue:
        highest = min(queue, key=lambda x: x[0])
        queue.remove(highest)
        return queue
    return None

def dequeue_low(queue):
    if queue:
        lowest = max(queue, key=lambda x: x[0])
        queue.remove(lowest)
        return queue
    return None

def peek_high(queue):
    if queue:
        return min(queue, key=lambda x: x[0])
    return None

def peek_low(queue):
    if queue:
        return max(queue, key=lambda x: x[0])
    return None

def dequeue_old(queue):
    if queue:
        queue.popleft()
        return queue
    return None

def dequeue_new(queue):
    if queue:
        queue.pop()
        return queue
    return None

print(enqueue(queue, 8, 'cafe'))
print(dequeue_high(queue))
print(dequeue_low(queue))
print(peek_high(queue))
print(peek_low(queue))
print(enqueue(queue, 10, 'sleep'))
print(dequeue_old(queue))
print(dequeue_new(queue))