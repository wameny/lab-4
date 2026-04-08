queue_fifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_fifo(item):
    queue_fifo.append(item)
    return queue_fifo

def dequeue_fifo():
    queue_fifo.pop(0)
    return queue_fifo

print('FIFO')
print(enqueue_fifo(4))
print(dequeue_fifo())
print(dequeue_fifo())
print(dequeue_fifo())
print(enqueue_fifo(89))

queue_lifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_lifo(item):
    queue_lifo.append(item)
    return queue_lifo

def dequeue_lifo():
    queue_lifo.pop()
    return queue_lifo

print('LIFO')
print(enqueue_lifo(4))
print(dequeue_lifo())
print(dequeue_lifo())
print(dequeue_lifo())
print(enqueue_lifo(89))