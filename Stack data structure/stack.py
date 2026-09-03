# 1. Push — Element Add Karna

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)


# 2. Pop — Top Element Remove Karna
stack = [10,20,30]

removed = stack.pop()
print("Removed" , removed)
print("Stack", stack)



# 3. Peek — Top Element Dekhna
stack = [10,20,30]

top = stack[-1]
print("Top Element", top)
print("Stack", stack)


# 4. isEmpty — Check Karna Stack Empty Hai Ya Nahi
stack = []

if not stack:
    print("Stack is empty")
    
else:
    print("Stack is not empty")
    
    

# Complete Example

# push
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# pop
removed = stack.pop()
print("Removed:", removed)

# peek

top = stack[-1]
print("Top Element:", top)
print("Stack:", stack)

# isEmpty

if not stack:
    print("Stack is not found")
    
else:
    print("Stack is found")
    
    
print(len(stack) == 0)



print("*********************")
class stack:
    
    def __init__(self):
        self.items = []
    
    def push (self , item ):
        self.items.append(item)
        
    def pop (self):
        
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek (self):
        
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty (self):
        return len(self.items) == 0
    
    def size (self):
        return len(self.items)
    
    def display (self):
        print("Stack (top > button):", self.items[::-1])
        
s = stack()
s.push(10)
s.push(20)
s.push(30)

print("After pushing 10,20,30")
s.display()

print("Top Element:", s.peek())
print("Popped Element:", s.pop())
print("After Popped")
s.display()

print("Total Size:", s.size())
print("Is Stack Empty:", s.is_empty())

        
            