# Simple Traversal
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x) # Output: 1 2 3 4 5
    
    
# Traversal using Index
print("\nTraversal using Index:")
for i in range(len(numbers)):
    print(i, numbers[i])
    
    
# Find Sum
print("\nFind Sum:")
marks = [60,75,90,65,80]
total = 0
for x in marks:
    total = total + x
print("Total:" , total) # Output: Total: 60 Total: 135 Total: 225 Total: 290 Total: 370


# Find Maximum
print("\nFind Maximum:")
marks = [60,75,90,65,80]
max_marks = marks[0]
for x in marks:
    if x > max_marks:
        max_marks = x 
print("Maximum Marks:" , max_marks) # Output: Maximum Marks: 90")


# (1) Right to Left Traversal 
print("\nRight to Left Traversal:")
marks = [60,75,90,65,80]
for x in reversed(marks):
    print(x) # Output: 80 65 90 75 60
    
    
# (2) Right to Left Traversal using Index
print("\n Right to left Traversal using Index:")
marks = [60,75,90,65,80]
for x in range(len(marks)-1, -1, -1):
    print(marks[x])
    
    
# (3) Right to Left Traversal using Slicing
print("\nRight to Left Traversal using Slicing:")
for x in marks[::-1]:
    print(x) 
    
    
# (4) Right to Left Traversal using While Loop
print("\nRight to Left Traversal using While Loop:")
marks = [60,75,90,65,80]
i = len(marks) - 1
while i >= 0:
    print(marks[i])
    i = i - 1
    
# Left to Right Traversal using While Loop
print("\nLeft to Right Traversal using While Loop:")
marks = [60,75,90,65,80]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
    
# Left to Right Traversal using Index
print("\nLeft to Right Traversal using Index:")
marks = [60,75,90,65,80]
for i in range(len(marks)):
    print(i, marks[i])
    
    
# Left to Right Traversal using Slicing
print("\nLeft to Right Traversal using Slicing:")
for x in marks:
    print(x)