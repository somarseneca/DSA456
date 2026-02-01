
## Function 1 

### Code

def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total


### Step 1: Variables
Let n represent the value of number.  
Let T(n) represent the number of operations.

### Step 2: Count Operations
total = 0                 # 1
for i in range(number):   # n + 1
    x = i + 1             # n
    total += x * x        # 2n
return total              # 1


### Step 3: T(n)
T(n) = 1 + (n + 1) + n + 2n + 1

### Step 4: Simplify
T(n) = 4n + 3

### Step 5: Result
Time Complexity: O(n)



## Function 2 Analysis

###  Code
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6

### Step 1: Variables
Let n represent the value of number.  
Let T(n) represent the number of operations.

### Step 2: Count Operations
(number * (number + 1) * (2 * number + 1)) // 6   # constant operations


### Step 3: T(n)
T(n) = 1

### Step 4: Simplify
T(n) = 1

### Step 5: Result
Time Complexity: O(1)



## Function 3 Analysis

### Code
def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp


### Step 1: Variables
Let n represent the length of the list.  
Let T(n) represent the number of operations.

### Step 2: Count Operations
The outer loop runs n times.  
The inner loop runs n times.  
Operations inside the loop are constant.

### Step 3: T(n)
T(n) = n × n

### Step 4: Simplify
T(n) = n²

### Step 5: Result
Time Complexity: O(n²)



## Function 4 Analysis

### Code
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total


### Step 1: Variables
Let n represent the value of number.  
Let T(n) represent the number of operations.

### Step 2: Count Operations
total = 1                 # 1
for i in range(1, number):# n
    total *= i + 1        # 2n
return total              # 1


### Step 3: T(n)
T(n) = 1 + n + 2n + 1

### Step 4: Simplify
T(n) = 3n + 2

### Step 5: Result
Time Complexity: O(n)



  ### -----------------
  Team member	Timing for fibonacci(39)	Timing for sum_to_number
    Sumaya Omar 0.8276335840055253          0.3002402469574008


### Summary

| function      | fastest | slowest | difference |
|--------------|---------|---------|------------|
| sum_to_goal  | 0.2921  | 0.3069  | 0.0148     |
| fibonacci    | 0.8014  | 0.8376  | 0.0363     |


### Reflection

Considering the solutions you saw in the lab 1 code, what differences did you see between the fastest and slowest versions

The biggest difference between the fastest and slowest versions was how the problem was solved. The slower Fibonacci solution used recursion, which repeats the same work many times. The faster version used a loop, which only calculated each value once. For the sum_to_goal function, solutions that used two loops were slower than solutions that used a set to find numbers faster.



Was there a difference in terms of the usage of space resources? Did one algorithm use more or less space (memory)?

Yes, there was a difference in memory usage. The recursive Fibonacci function used more memory because each function call was stored on the call stack. The loop-based Fibonacci function used less memory because it did not need extra function calls. The sum_to_goal function that used a set needed some extra memory, but it ran faster than the version that used nested loops.


What sort of conclusions can you draw based on your observations?

These results show that the way an algorithm is written can greatly affect its speed and memory usage. Recursive solutions can be slower and use more memory, while loop-based solutions are usually faster. Using the right data structures can make programs run more efficiently.
