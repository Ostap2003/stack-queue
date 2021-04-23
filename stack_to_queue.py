"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    '''Convert stack to queue, without changing given stack
    peek of the stack is the first element in the queue'''
    queue = ArrayQueue()
    stack_copy = ArrayStack(stack)

    while len(stack_copy) != 0:
        queue.add(stack_copy.pop())

    return queue
