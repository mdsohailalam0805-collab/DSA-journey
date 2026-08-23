# Complexity Analysis

Complexity Analysis is used to measure the performance of an algorithm based on its **time and space requirements** as the input size increases.

## Time Complexity

Time Complexity tells us how the number of operations grows with input size `n`.

| Big O | Meaning |
|-------|---------|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(2ⁿ) | Exponential |

### Examples

**O(1) — Constant**

numbers = [10,20,30,40,50,60,70,80,90,100]
print(numbers[0])


O(n) — Linear

for x in numbers:
    print(x)


O(n²) — Quadratic

for i in numbers:
    for j in numbers:
        print(i, j)


O(log n) — Logarithmic
Used when the problem is repeatedly reduced, such as Binary Search.

## Space Complexity

Space Complexity tells us how much extra memory an algorithm uses.

O(1) — Constant Space

maximum = numbers[0]
for x in numbers:
    if x > maximum:
        maximum = x


O(n) — Linear Space

new_list = []

for x in numbers:
    new_list.append(x)



## Important Rules

Constants are ignored: O(2n) → O(n)
Keep the fastest-growing term: O(n) + O(n²) → O(n²)
Sequential loops → Add
Nested loops → Multiply
Time Complexity → Amount of work
Space Complexity → Extra memory