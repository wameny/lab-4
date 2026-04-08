queue_fifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_fifo(item):
    queue_fifo.append(item)
    return queue_fifo

def dequeue_fifo():
    if queue_fifo:
        queue_fifo.pop(0)
        return queue_fifo
    return None

def peek_fifo():
    if queue_fifo:
        return queue_fifo[0]
    return None

print('FIFO')
print(enqueue_fifo(4))
print(dequeue_fifo())
print(dequeue_fifo())
print(dequeue_fifo())
print(enqueue_fifo(89))
print(peek_fifo())

queue_lifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_lifo(item):
    queue_lifo.append(item)
    return queue_lifo

def dequeue_lifo():
    if queue_lifo:
        queue_lifo.pop()
        return queue_lifo
    return None

def peek_lifo():
    if queue_lifo:
        return queue_lifo[-1]
    return None

print('LIFO')
print(enqueue_lifo(4))
print(dequeue_lifo())
print(dequeue_lifo())
print(dequeue_lifo())
print(enqueue_lifo(89))
print(peek_lifo())
