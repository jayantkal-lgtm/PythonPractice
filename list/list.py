name = ["Alice", "Bob", "Charlie"]
print(name)

empData = {"name": "Alice", "age": 30, "city": "New York"}

"""
List is ordered : The data elements of list maintain their order of insertion.
List is Mutable (Changeable) :  Lists in Python allow modification of their elements after creation.
Heterogeneous (Different Data Types): A single list can store multiple data types like integers, strings, floats, and even another list.
Contains Duplicates: List is a data structure that can store duplicate values.

indexe based opration --> index 1 will get second element form the list
it accepted index form -1 also -1 means last element of the list and -2 means second last element of the list

slicing opration is also possible in list -> start index and end index is given and it will return the elements from start index to end index -1
In oprator : returns True if the specified item is present in the list, otherwise False.
count method : returns the number of times the specified item appears in the list. count(item)
set the order of the list using sort method : sort() method sorts the list in ascending order by default. You can also use the reverse=True parameter to sort in descending order.
Reverse opration is also possible using reverse method : reverse() method reverses the elements of the list in place.
remove value form the list using index : pop() method removes the element at the specified position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.
del keyword is used to delete the list completely.
del keyword using index is used to delete the element at the specified index.
copy method is used to create a copy of the list. It returns a shallow copy of the list.
list() method is used to create a list from an iterable. It can be used to convert other data types (like tuples, sets, or strings) into a list.

Adding Elements to the List
1. append() method : The append() method adds a single element to the end of the list.
2. extend() method : The extend() method adds multiple elements to the end of the list.
3. insert() method : The insert() method allows you to add an element at a specific index in the list. It takes two arguments: the index where you want to insert the element and the value of the element itself.

Removing Elements from the List
1. remove() method : The remove() method removes the first occurrence of a specified value from
    the list. If the value is not found, it raises a ValueError.
2. pop() method : The pop() method removes and returns the element at a specified index. If no index is provided, it removes and returns the last element of the list.
3. del statement : The del statement can be used to remove an element at a specific index

Iteration over list using for loop : You can iterate over the elements of a list using a for loop. This allows you to access each element one by one and perform operations on them.

Finding the Largest and Smallest Number in a List
To find the largest and smallest number in a list, we can make use of max() and min() functions as shown in the following example:

"""

print(name[0])  # Output: Alice
name[0] = "Rajesh" # Modifying the first element
print(name)  # Output: ['Rajesh', 'Bob', 'Charlie']

name.append("David")  # Adding a new element
print(name)  # Output: ['Rajesh', 'Bob', 'Charlie', 'David]

# I want to add at sepecific index insert method index position and value that need to be added
name.insert(1, "Ram")  # Inserting at index 1
print(name)  # Output: ['Rajesh', 'Ram', 'Bob', 'Charlie', 'David']

name.remove("Bob")  # Removing an element by value
print(name)  # Output: ['Rajesh', 'Ram', 'Charlie', 'David]

len(name)  # Output: 4

# Accessing elements using negative indexing
print(name[-1])  # Output: David
print(name[-2])  # Output: Charlie

# Slicing
print(name[1:3])  # Output: ['Ram', 'Charlie'] (slicing from index 1 to 2)
print(name[1:4])  # Output: ['Ram', 'Charlie', 'David'] (slicing from index 1 to 3) 
print(name[0:])  # Output: ['Rajesh', 'Ram', 'Charlie', 'David'] (slicing from index 0 to end)  

# in operator : returns True if the specified item is present in the list, otherwise False.
print("Ram" in name)  # Output: True
print("Bob" in name)  # Output: False

# count method : returns the number of times the specified item appears in the list. count(item)
print(name.count("Ram"))  # Output: 1
print(name.count("Bob"))  # Output: 0

# sort() method sorts the list in ascending order by default. You can also use the reverse=True parameter to sort in descending order.
name.sort()  # Sorting in ascending order
print(name)  # Output: ['Charlie', 'David', 'Ram', 'Rajesh']
name.sort(reverse=True)  # Sorting in descending order
print(name)  # Output: ['Rajesh', 'Ram', 'David', 'Charlie']

# reverse() method reverses the elements of the list in place.
name.reverse()  # Reversing the list
print(name)  # Output: ['Charlie', 'David', 'Ram', 'Rajesh']

# pop() method removes the element at the specified position in the list, and returns it. If no index is specified, pop() removes and returns the last item in the list.
last_element = name.pop()  # Removing and returning the last element
print(last_element)  # Output: Rajesh
print(name)  # Output: ['Charlie', 'David', 'Ram']
popped_element = name.pop(1)  # Removing and returning the element at index 1
print(popped_element)  # Output: David      
print(name)  # Output: ['Charlie', 'Ram']

#list() method is used to create a list from an iterable. It can be used to convert other data types (like tuples, sets, or strings) into a list.
tuple_data = (1, 2, 3)
list_from_tuple = list(tuple_data)  # Converting tuple to list
print(list_from_tuple)  # Output: [1, 2, 3]


# Min and max functions to find the smallest and largest number in a list
numbers = [5, 2, 8, 1, 9]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1