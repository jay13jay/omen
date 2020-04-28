#!/usr/bin/env python3

'''
A queue object to broker data and order ingress/egress
'''

import Queue as queue

class Broker:
  def __init__(self):
    self.queue = []

  def isEmpty(self):
    if len(self.queue) > 0:
      print("q not empty")
      return 0
    elif len(self.queue) < 0:
      print("q somehow less than 0... somethings wrong")
      return 2
    elif len(self.queue) == 0:
      print("q is empty")
      return 1

  def isFull(self):
    if len(self.queue) >= 100:
      return(True)
    elif len(self.queue) <= 0:
      return(False)
    else:
      return(None)

  def get_queue(self):
    isEmpty = self.isEmpty()
    print(isEmpty)

  def add_queue(self,element):
    self.queue.append(element)

  def queue_size(self):
    return self.queue.size()

  def fill_q(self):
    count = 0
    while self.queue_size < 99:
      self.queue.add_queue(count)  
      print("current q:\t\t", get_queue())
      count += 1


def main():
  myq = Broker()
  myq.get_queue()

  # Fill queue
  count = 0
  print("status:", myq.isFull())
  while not myq.isFull():
    print("Queue not full, adding...")
    myq.fill_q()
    print("current queue:\t", myq.get_queue())
    myq.add_queue(count)





if __name__ == "__main__":
    main()