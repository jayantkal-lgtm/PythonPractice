# unique data stored in set , there is no order in set, it is unordered collection of data.
# example : {1, 2, 3, 4, 5}

"""

A set has the following features:

Unordered: Elements are not stored in any specific order.
Unindexed: We cannot access elements using an index.
No Duplicate Elements: Each element in a set is unique.
Mutable: We can add or remove elements after the set is created.

Creating a Set
- Using curly braces {}
- Using the set() function

1. add() method is used to add a single element to a set. If the element already exists, it will not be added again.
2. update() method is used to add multiple elements to a set. will pass on desired values in the form of list, tuple, or another set.
3. remove() method is used to remove a specific element from a set. If the element does not exist, it will raise a KeyError.
4. discard() method is used to remove a specific element from a set. If the element does not exist, it will not raise an error.
5. pop() method is used to remove and return an arbitrary element from a set. If the set is empty, it will raise a KeyError.
6. del keyword can be used to delete an entire set. delete based on index is not possible in set as it is unordered collection of data. hence, you cannot access elements by index or slice a set.
7. clear() method is used to remove all elements from a set, making it an empty set.
8. len() function is used to get the number of elements in a set.
9. in operator is used to check if a specific element exists in a set. It returns True if the element is found, otherwise False.
10. union() method is used to combine two sets and return a new set containing all unique elements from both sets.
11. intersection() method is used to find the common elements between two sets and return a new set containing those elements.

"""

# Set Examples AND how to create a set
empId = {101, 102, 103, 104, 105}
studentId = {201, 202, 203, 204, 205, 104, 105}
mixedset = {12, 34, 56, 78, 90, "hello", "world", 12.34, True}
names = {"Alice", "Bob", "Charlie", "David"}

# using set() function
list = [1, 2, 3, 4, 5,6, 1,3, 4, 5]
set_from_list = set(list)


# accessing elements in a set using for loop
for emp in empId:
    print(emp)

# adding elements to a set
empId.add(106)  # Adding a single element
print(empId)

# update the set with multiple elements
empId.update([107, 108, 109])  # Adding multiple elements
print (empId)
