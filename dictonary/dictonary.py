"""
Dictonary in Python has a following properties:
1. Unordered: Dictonary is an unordered collection of data. It does not maintain
2. Key-Value Pair: Each element in a dictonary is stored as a key-value pair. The key is unique, and the value can be of any data type.
3. Mutable: Dictonary is mutable, meaning you can add, remove, or modify elements after the dictonary is created.
4. Dynamic Size: Dictonary can grow or shrink in size as elements are added or removed.
5. insertion order is preserved in dictonary from python 3.7 onwards, but it is not guaranteed in earlier versions.

methods available for dictonary:
1. keys(): Returns a view object that displays a list of all the keys in the dictonary.
2. values(): Returns a view object that displays a list of all the values in the dictonary.
3. items(): Returns a view object that displays a list of tuples, where each tuple contains a key-value pair from the dictonary.
4. get(key, default): Returns the value associated with the specified key. If the key does not exist, it returns the default value (if provided) or None.
5. update(other_dic): Updates the dictonary with key-value pairs from another dictonary or an iterable of key-value pairs.
6. pop(key, default): Removes the specified key and returns its value. If the key does not exist, it returns the default value (if provided) or raises a KeyError.
7. popitem(): Removes and returns an arbitrary key-value pair from the dictonary. Raises a KeyError if the dictonary is empty.
8. clear(): Removes all key-value pairs from the dictonary, making it empty.
9. dict(): Creates a new dictonary. It can be used to create an empty dictonary or to convert other data types (like lists or tuples) into a dictonary.
10 copy(): Returns a shallow copy of the dictonary. It creates a new dictonary with the same key-value pairs as the original dictonary.
11. get(key, default): Returns the value associated with the specified key. If the key does not exist, it returns the default value (if provided) or None.

"""


# dictonary has a key and value pair
dic = {
    "name": "Alice", 
    "age": 25, 
    "city": "New York"
    }

student = {
    "name": "Bob",
    "age": 30,
    "courses": ["Math", "Science", "History"]
    }



carData = {
    "maker": "Toyota",   
    "model": "Camry",
    "carYear": 2020,
     "carColor": ["Red", "Blue", "Black"]
}


    
print(student.items())
print('Student Keys:', student.keys())
print('Student Values:', student.values())


print('Car Data:', carData)
print('Car Keys:', carData.keys())
print('Car Values:', carData.values())
print('Car Items:', carData.items())