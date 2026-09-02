# Remove Duplicates

numbers = [1, 1, 2, 2, 3, 4, 5, 5, 6]

left = 0

for right in range(1, len(numbers)):
    
    if numbers[left] != numbers[right]:
        left += 1
        
        numbers[left] = numbers[right]
        
print(numbers[:left + 1]) # Output: [1, 2, 3, 4, 5, 6] 



# Remove Duplicates
def clean(names):
    left = 0
    
    for right in range(1, len(names)):
        
        if names [left] != names[right]:
            left = left + 1
            names[left] = names[right]
            
    return left + 1

names = ["sohail", "sohail", "saif", "saif", "faiz", "faiz", "altamash"]

count = clean(names)
print("count of unique names:", names[:count]) # Output: count of unique names: 4





# Slow and Fast Pointer — Find Middle Element
def find_middle_element(numbers):
    slow = 0
    fast = 0
    while fast < len(numbers) and fast + 1 < len(numbers):
        slow = slow + 1
        fast = fast + 2
    return numbers[slow]

numbers = [1, 2, 3, 4, 5]
middle_element = find_middle_element(numbers)
print("Middle Element:", middle_element) # Output: Middle Element: 3



# Find a Subarray
def find_subarray(numbers, target):
    left = 0
    current_sum = 0
    
    for right in range(len(numbers)):
        current_sum += numbers[right]
        
        while current_sum > target:
            current_sum -= numbers[left]
            left += 1
            
        if current_sum == target:
            return numbers[left:right + 1]
        
    return [] # Return an empty list if no subarray is found

numbers = [1,2,5,6,8,10,12] 
target = 15

result = find_subarray(numbers, target)

if result:
    print("Subarray found:", result) 
else:
    print("No subarray found with the given target.")
    
    
    
    
    
numbers = [1, 2, 3, 4, 5]
target = 11

left = 0
current_sum = 0

for right in range(len(numbers)):
    current_sum += numbers[right]

    while current_sum > target:
        current_sum -= numbers[left]
        left += 1

    if current_sum == target:
        print(numbers[left:right + 1])
    else:
        print("No subarray found with the given target.")