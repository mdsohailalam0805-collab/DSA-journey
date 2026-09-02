numbers = [3,1,4,1,5,9,2]
k = 3

window_sum = sum(numbers[:k])
max_sum = window_sum

for i in range(k, len(numbers)):
    
     window_sum = window_sum - numbers[i - k]
     window_sum = window_sum + numbers[i]
     
     max_sum = max(max_sum, window_sum)
     
print(max_sum)




numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(numbers[:k])
max_sum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i - k]
    window_sum = window_sum + numbers[i]

    max_sum = max(max_sum, window_sum)

print(max_sum)