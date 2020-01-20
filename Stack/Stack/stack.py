class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def print_stack(self):
        return self.items

s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.pop()
s.push('D')

print(s.print_stack())
stacks = s.print_stack()

for stack in stacks:
    print(stack)
