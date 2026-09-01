def find_two_numbers(numbers, target):
    
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return (numbers[left], numbers[right])
        
        elif current_sum < target:
            left = left + 1
            
        else:
            right = right - 1
            
    return [] # Return an empty list if no pair is found

numbers = [1, 2, 3, 4, 6]
target = 10
result = find_two_numbers(numbers, target)
if result:
    print("Pair found:", result)