# How to open the file and how to handle this 

file = open('youtube.txt', 'w')

try: 
    file.write('My name is jayant Kale')
finally:
    file.close()

with open('youtube1.txt','w') as file:
    file.write('chai or python')