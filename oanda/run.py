#!/usr/bin/python
import daemon
import time

# Create queue object
class Queue: 
  def __init__(self):
    self.queue = []

  def dequeue(self):
    return self.queue.pop(0) # probably want to return what you dequeue.

  def enqueue(self,element):
    self.queue.append(element)


q=Queue()
# q.enqueue('dog')
# q.enqueue('cat')


def logit(data):
  fp = open('test.log','a')
  fp.write(data)
  fp.close()

daemon.createDaemon()
count = 0
exit = 1
while exit == 1:
  time.sleep(2)
  # add to q if count < 5
  if count <= 5:
    _data = str("Entering %s into queue\n" % (count))
    q.enqueue(_data)
    logit(_data)
    count += 1
  elif count <=10:
    _data = str("removing %s from queue\n" % (q.dequeue()))
    print(_data)
    count += 1
  elif count > 10:
    exit(0)
  