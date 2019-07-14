from StackAndQueue import Stack, Queue # With StackAndQueue.py in the same directory

# Example usages:        

def reverse(stack):
    tempQueue = Queue()
    while not stack.isEmpty():
        tempQueue.enqueue(stack.pop())
    while not tempQueue.isEmpty():
        stack.push(tempQueue.dequeue())

s = Stack([1, 2, 3])
print(s)
reverse(s)
print(s)


def removeBottom(stack): # intentionally buggy code, answer: reverse order
    tempQueue = Queue()
    while not stack.isEmpty():           
        element = stack.pop();
        if stack.size() == 0: #if last element was popped, don't queue it
            break
        tempQueue.enqueue(element);
    while not tempQueue.isEmpty():
        stack.push(tempQueue.dequeue()) #put elements back in stack
        
s = Stack([1, 2, 3])
print(s)
removeBottom(s)
print(s)

def printStack(stack):
  #how does this temp stack help replace the original? Draw it out!
    temp = Stack()
    while not stack.isEmpty():
        temp.push(stack.peek())
        print(stack.peek())  #could also say print temp.peek() 
        stack.pop()
    while not temp.isEmpty():
        stack.push(temp.pop())
s = Stack([1, 2, 3])
print(s)
printStack(s)

stack = Stack([3, 4, 5])
product = stack.pop()
while not stack.isEmpty():
  product *= stack.pop()
print(product)
