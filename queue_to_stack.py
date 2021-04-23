"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    '''Convert queue to stack, without modifying the queue
    peek of the stack must be first element of the queue'''
    stack = ArrayStack()
    queue_copy = ArrayQueue(queue)

    while len(queue_copy) != 0:
        stack.push(queue_copy.remove(len(queue_copy) - 1))

    return stack
