"""
Yoputube Links -
https://www.youtube.com/watch?v=HVSWmjcAIa8&t=54s

There are two type of functions in Python: 
1. Built-in functions: These are functions that are provided by Python itself, such as print(), len(), and type().
2. User-defined functions: These are functions that are defined by the user to perform specific tasks.

Build in functions Examples:
1. print(): Prints the specified message to the console.
2. len(): Returns the length of an object.
3. type(): Returns the type of an object.
4. int(): Converts a value to an integer.
5. str(): Converts a value to a string.
6. float(): Converts a value to a floating-point number.
7. list(): Creates a new list.
8. dict(): Creates a new dictionary.
9. set(): Creates a new set.
10. input(): Reads a line of input from the user.

DSA point of view below build in functions are important -
1. len(): Returns the length of an object.
DSA Use Case: Used constantly for loop boundaries, checking base cases in recursion, or finding array/string sizes.
example:
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

2. sorted(): Returns a new sorted list from the elements of any iterable.
DSA Use Case: Frequently used to sort arrays or lists before applying algorithms that require ordered data.
example:
my_list = [5, 2, 9, 1, 5, 6]
print(sorted(my_list))  # Output: [1, 2, 5, 5, 6, 9]

intervals = [[1, 3], [2, 6], [8, 10]]
sorted_intervals = sorted(intervals, key=lambda x: x[0])
print(sorted_intervals)  # Output: [[1, 3], [2, 6], [8, 10]]

3. min() and max() return the smallest and largest item in an iterable, respectively.
DSA Use Case: Commonly used to find the minimum or maximum value in an array or list, which is often required in optimization problems.
example:
my_list = [5, 2, 9, 1, 5, 6]
print(min(my_list))  # Output: 1
print(max(my_list))  # Output: 9

4. sum() returns the sum of all items in an iterable.
DSA Use Case: Often used to calculate the total of elements in an array or list, which is common in problems involving cumulative sums or prefix sums.
example:
my_list = [5, 2, 9, 1, 5, 6]
print(sum(my_list))  # Output: 28

5. any() returns True if any element of the iterable is true. If the iterable is empty, returns False.
DSA Use Case: Useful for checking if at least one element in a collection satisfies a certain condition, often used in filtering or validation scenarios.
example:
my_list = [0, 0, 1, 0]
print(any(my_list))  # Output: True

6. all() returns True if all elements of the iterable are true. If the iterable is empty, returns True.
DSA Use Case: Useful for checking if all elements in a collection satisfy a certain condition, often used in validation or constraint checking.
example:
my_list = [1, 2, 3, 4]
print(all(my_list))  # Output: True

7. zip() returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
DSA Use Case: Useful for iterating over multiple sequences in parallel, often used in problems involving pairwise comparisons or combining data from different sources.
example:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

8. enumerate() returns an iterator of tuples containing indices and values from an iterable.
DSA Use Case: Useful for iterating over a sequence while keeping track of the index, often used in problems where the position of elements matters.
example:
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c

9. reversed() returns a reverse iterator over the elements of a sequence.
DSA Use Case: Useful for iterating over a sequence in reverse order, often used in problems where backward traversal is required.
example:
my_list = [1, 2, 3, 4]
for value in reversed(my_list):
    print(value)
# Output:
# 4
# 3
# 2
# 1

10. sorted() returns a new sorted list from the elements of any iterable.
DSA Use Case: Useful for sorting elements in ascending or descending order, often used in problems that require ordered data.
example:
my_list = [5, 2, 9, 1, 5, 6]
print(sorted(my_list))  # Output: [1, 2, 5, 5, 6, 9]
print(sorted(my_list, reverse=True))  # Output: [9, 6, 5, 5, 2, 1]



As QA point of view, these built-in functions are essential for efficiently handling common tasks in Python,
such as finding minimum and maximum values, summing elements, checking conditions, iterating with indices, reversing sequences, and sorting data.
Understanding their use cases and examples can significantly improve code readability and performance.

1. Data Inspection & Type Safety (isinstance, type, len, callable)
Example: isinstance(object, classinfo)
QA Use Case: Critical in API test assertions and data-driven frameworks to safely verify JSON response schemas or configuration types before performing operations.
Interview Value: Shows you write defensive, resilient test code rather than assuming data types.

2. len(s)
QA Use Case: Validating that an API list endpoint returns the expected count, or checking that a web table / mobile recycler view contains rows.
Interview Value: Demonstrates attention to detail and the ability to write tests that verify the completeness of data structures.

3. callable(obj)
QA Use Case: Ensuring that a function or method exists and can be invoked before attempting to call it, preventing runtime errors in test scripts. 
Useful in dynamic test hooks, custom fixtures, or passing callback functions into LangChain agents and tool execution pipelines.
Interview Value: Highlights your ability to write robust and error-resistant test code.

example:
my_list = [1, 2, 3]
print(isinstance(my_list, list))  # Output: True
print(type(my_list))  # Output: <class 'list'>
print(len(my_list))  # Output: 3
print(callable(len))  # Output: True


"""