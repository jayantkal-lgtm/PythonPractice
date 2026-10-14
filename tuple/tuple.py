# tuple is similar to list but it is immutable, once created you cannot modify it. tuple is ordered collection of data.
# It is defined using parentheses () instead of square brackets [].
# It accepts duplicate values and can contain elements of different data types.

"""
A tuple has the following features:
1. Ordered: Elements are stored in a specific order.
2. Indexed: Each element in a tuple has a unique index, starting from 0.
3. Immutable: Once a tuple is created, its elements cannot be modified, added, or removed.
4. edit and delete is not possible in tuple, but you can create a new tuple with the desired changes.
5. Accepts Duplicate Values: A tuple can contain duplicate values.

Methods available for tuple:
1. count(): Returns the number of occurrences of a specified element in the tuple.
2. index(): Returns the index of the first occurrence of a specified element in the tuple.

"""

empId = (101, 102, 103, 104, 105)

# How to change elements in a tuple
# empId[0] = 201  # This will raise an error because tuples are immutable. 
# example of creating a new tuple with modified values

duplicate_emp = list(empId)  # Convert tuple to list
duplicate_emp[0] = 201  # Modify the first element in the list
empId2 = tuple(duplicate_emp)  # Convert the list back to a tuple
for emp in empId2:
    print(emp)