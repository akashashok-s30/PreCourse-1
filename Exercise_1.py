# Time Complexity : O(1)
# Space Complexity : O(len(stack))

class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
         self.stack = []

     def isEmpty(self):
         if self.stack:
           return False
         return True

     def push(self, item):
         self.stack.append(item)

     def pop(self):
        return self.stack.pop(len(self.stack)-1)
        
     def peek(self):
       return self.stack[len(self.stack)-1]
        
     def size(self):
       return len(self.stack)
         
     def show(self):
         return (list(self.stack))

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())