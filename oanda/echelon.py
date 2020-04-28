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
    elif len(self.queue) < 0:
      print("q somehow less than 0... somethings wrong")
    elif len(self.queue) == 0:
      print("q is empty")
      return(True)

  def get_queue(self):
    isEmpty = self.isEmpty()
    print(isEmpty)

  def add_queue(self,element):
    self.add_queue.append(element)

  def queue_size(self):
    return self.queue.size()


def main():
  myq = Broker()
  print("Current Q:\t"+ str(myq.get_queue()))




if __name__ == "__main__":
    main()