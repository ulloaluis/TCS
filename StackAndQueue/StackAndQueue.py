# Stack/Queue implementations for pedagogical use.
# Note that these implementations utilize list methods that
# python uses to mirror stack/queue operations.
# See: https://glot.io/snippets/fe2z3pzd1q
class Stack:
    def __init__(self, initializers = []):
        self.stack = initializers[:]
        # Given [1, 2, 3], 3 is the top, 1 is the bottom

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
            
    def __str__(self):
        return "Stack(" + str(self.stack)[1:-1] + ")"

class Queue:
    def __init__(self, initializers = []):
        self.queue = initializers[:]
        # Given [1, 2, 3], 1 is the front, 3 is the back

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
        
    def isEmpty(self):
        return len(self.queue) == 0
        
    def __str__(self):
        return "Queue(" + str(self.queue)[1:-1] + ")"
        
