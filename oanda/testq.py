#!/usr/bin/env python3

class Queue: 

    def __init__(self):
        self.queue = []

    def dequeue(self):
        return self.queue.pop(0) # probably want to return what you dequeue.

    def enqueue(self,element):
        self.queue.append(element)


q=Queue()
q.enqueue('dog')
q.enqueue('cat')
print(repr(q))
print(q)
print(q)