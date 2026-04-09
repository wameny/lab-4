queue_fifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_fifo(queue, item):
    queue.append(item)
    return queue

def dequeue_fifo(queue):
    if queue:
        queue.pop(0)
        return queue
    return None

def peek_fifo(queue):
    if queue:
        return queue[0]
    return None

print('FIFO')
print(enqueue_fifo(queue_fifo, 4))
print(dequeue_fifo(queue_fifo))
print(dequeue_fifo(queue_fifo))
print(dequeue_fifo(queue_fifo))
print(enqueue_fifo(queue_fifo, 89))
print(peek_fifo(queue_fifo))

queue_lifo = [2, 6, 8, 2, 45, 6, 0, 2]

def enqueue_lifo(queue, item):
    queue_lifo.append(item)
    return queue_lifo

def dequeue_lifo(queue):
    if queue_lifo:
        queue_lifo.pop()
        return queue_lifo
    return None

def peek_lifo(queue):
    if queue_lifo:
        return queue_lifo[-1]
    return None

print('LIFO')
print(enqueue_lifo(queue_lifo, 4))
print(dequeue_lifo(queue_lifo))
print(dequeue_lifo(queue_lifo))
print(dequeue_lifo(queue_lifo))
print(enqueue_lifo(queue_lifo, 89))
print(peek_lifo(queue_lifo))
