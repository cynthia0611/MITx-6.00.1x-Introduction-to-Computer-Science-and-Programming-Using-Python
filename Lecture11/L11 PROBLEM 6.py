"""
Queue class
 When you want to get something off the end of a queue,
 you get the item that has been in there the longest,
'first-in-first-out', or FIFO,
Three methods:
__init__: initialize your Queue
(think: how will you store the queue's elements?
You'll need to initialize an appropriate object attribute in this method)

insert: inserts one element in your Queue

remove: removes (or 'pops') one element from your Queue and returns it.
If the queue is empty, raises a ValueError.
"""

class Queue(object):
    def __init__(self):
        self.qlist = []

    def insert(self, e):
        self.qlist.append(e)
            
    def remove(self):
        try:
            return self.qlist.pop(0)
        except:
            raise ValueError()

##    def remove(self):
##        "Removes an element from the attribute list"
##        # Check if the list is empty; if so then raise a ValueError
##        if self.qlist == []:
##            raise ValueError()
##        else:
##            # Otherwise we want to remove the first element from the list
##            # and return that to the user.
##            element = self.qlist[0]
##            self.qlist.remove(element)
##            return element
##            # Could also do this in 1 line:
##            # return self.qlist.pop(0)
            
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.qlist]) + '}'    
        
queue = Queue()
queue.insert(5)
queue.insert(6)
##print queue
print queue.remove()#5
queue.insert(7)
print queue.remove()#6
##print queue
print queue.remove()#7
