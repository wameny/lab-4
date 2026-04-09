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

def dequeue(queue, type='highest'):
    if queue:
        if type == 'highest':
            highest = min(queue, key=lambda x: x[0])
            queue.remove(highest)
            return queue
        if type == 'lowest':
            lowest = max(queue, key=lambda x: x[0])
            queue.remove(lowest)
            return queue
        if type == 'oldest':
            queue.popleft()
            return queue
        if type == 'newest':
            queue.pop()
            return queue
    return None

def peek(queue, type='highest'):
    if queue:
        if type == 'highest':
            return min(queue, key=lambda x: x[0])
        if type == 'lowest':
            return max(queue, key=lambda x: x[0])
        if type == 'oldest':
            return queue[0]
        if type == 'newest':
            return queue[-1]
    return None

print(enqueue(queue, 8, 'cafe'))
print(dequeue(queue, 'highest'))
print(dequeue(queue, 'lowest'))
print(peek(queue, 'highest'))
print(peek(queue, 'lowest'))
print(enqueue(queue, 10, 'sleep'))
print(peek(queue, 'oldest'))
print(peek(queue, 'newest'))
print(dequeue(queue, 'oldest'))
print(dequeue(queue, 'newest'))