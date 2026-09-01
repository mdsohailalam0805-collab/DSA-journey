marks = [90, 85, 60, 95, 87]
print("Marks:", marks)

print(marks[0])  # Accessing the first element
print(marks[4])  # Accessing the last element

marks.append(92)  # Adding a new mark
print("Updated Marks:", marks)

marks[2] = 75  # Modifying the third mark
print("Modified marks:", marks)

marks.remove(92) #Removing a mark
print("Marks After Removal:", marks)

marks.insert(2,80) # Inserting a mark at index 2
print("Marks After Insertion:", marks)

marks.pop() # Removing the last mark
print("Marks After Popping Last Element:", marks)

marks.pop(1) # Removing the mark at index 1
print("Marks After Popping Element at Index 1:", marks)

print(marks[1:4]) # Slicing the list to get marks from index 1 to 3
print(marks[::-1]) # Reversing the list
print(marks[::2]) # Getting every second mark
