
# Part A: Questions about the video

## 1. What sorting algorithm was the speaker trying to improve?

The speaker was trying to improve `std::sort`, which is usually based on a sorting method called introsort. Introsort combines quicksort, heapsort, and insertion sort.


## 2. At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?

Visual Studio switches to insertion sort when the partition size reaches 32 elements.



## 3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?

GNU switches to insertion sort when the partition size reaches 16 elements.



## 4. Regular insertion sort does a linear search backwards from end of array for correct spot to insert. According to the speaker, why does switching to a binary search not improve performance?

Binary search reduces the number of comparisons, but insertion sort mostly spends time moving elements, not comparing them. Even if the position is found faster, the elements still need to be shifted one by one.

Binary search also adds more branching (more “if” statements), which can slow down the CPU.



## 5. Describe what is meant by branch prediction. (this may require further research)

Branch prediction is when the CPU tries to guess the result of an `if` statement before it finishes checking it.

If the CPU guesses correctly, the program runs faster.  
If it guesses wrong, it has to redo work, which slows the program down.



## 6. What is meant by the term informational entropy? (this may require further research)

Informational entropy is a term created by Claude Shannon. It describes the amount of randomness or disorder in data.

In sorting:
- A random list has high entropy.
- A sorted list has low entropy.

Sorting works by reducing entropy and organizing the data.



## 7. Speaker suggests the following algorithm:  
o make_heap()  
o unguarded_insertion_sort()  

He suggests that by doing make_heap() first, you can do something called unguarded_insertion_sort(). Please explain what unguarded_insertion_sort() is and why it is faster than regular insertion sort. How does performing make_heap() allow you to do this?

Normal insertion sort checks that it does not go past the beginning of the array. This extra check is called a guard.

Unguarded insertion sort removes that check because it assumes there is already a very small value at the beginning of the array (called a sentinel).

Why it is faster:
- It removes one `if` check inside the loop.
- Fewer checks mean fewer CPU prediction mistakes.
- The loop becomes simpler and runs faster.

The speaker suggests using `make_heap()` first. This helps guarantee a safe smallest value exists, so the guard is no longer needed.



## 8. The speaker talks about incorporating your conditionals into your arithmetic. What does this mean? Provide an example from the video and explain how the conditional is avoided.

It means removing `if` statements and using math operations instead.

For example, instead of:

If a < b, choose a, else choose b.

You can sometimes use arithmetic operations to calculate the result without using an `if` statement.

This reduces branching and helps avoid CPU prediction errors.



## 9. The speaker talks about a bug in gnu's implementation. Describe the circumstances of this bug.

The bug happened because the algorithm assumed there was always a safe smallest value (a sentinel). In some special cases, this was not true.

Because of this incorrect assumption, the program could try to access memory outside the array, which causes errors.



## 10. The speaker shows several graphs about what happens as the threshold increases using his new algorithm. The metric of comparison is increased, and the metric of moves is increased, but time drops... What metric does the author think is missing? Describe the missing metric he speaks about in the video. What is the metric measuring?

The missing metric was branch mispredictions.

Even though comparisons and moves increased, the program ran faster because it reduced branch mispredictions.

Branch mispredictions measure how often the CPU guesses the wrong path in a conditional statement. When the CPU guesses wrong, it has to redo work, which slows down the program.



## 11. What does the speaker mean by fast code is left-leaning?

It means writing conditions so that the most common case happens first.

CPUs often predict that branches will not happen. If your code matches what the CPU expects, it runs faster.



## 12. What does the speaker mean by not mixing hot and cold code?

Hot code is code that runs very often (like inside loops).  
Cold code is code that runs rarely (like error handling).

If you mix them together, performance can decrease. Keeping them separate helps the CPU run more efficiently.



# Part B: Reflection

## 1. What did you find most challenging to understand in the video?

The hardest concept to understand was how branch prediction affects performance. I am used to thinking about sorting in terms of Big-O notation like O(n log n). It was challenging to understand how hardware features like pipelines and branch mispredictions can have a bigger impact than the number of comparisons.



## 2. What is the most surprising thing you learned that you did not know before?

The most surprising thing I learned was that an algorithm can do more comparisons and more moves but still run faster. I always thought fewer operations automatically meant better performance. This video showed that reducing branch mispredictions can be more important.



## 3. Has the video given you ideas on how you can write better/faster code? If yes, explain what you plan to change when writing code in the future. If not, explain why not.

Yes, it has.

In the future, I will:
- Reduce unnecessary `if` statements inside loops.
- Think about how often conditions are true or false.
- Keep frequently used code separate from rarely used code.
- Consider how the CPU executes instructions, not just algorithm complexity.

Before watching this video, I focused mostly on algorithm complexity. Now I understand that writing fast code also requires understanding how computers process instructions.