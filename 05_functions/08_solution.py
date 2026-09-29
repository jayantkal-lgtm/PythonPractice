#Create a function that accepts any number of keyword arguments and prints them in the format key: value

def print_kargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kargs(name = "jayant", surname="kale")
print_kargs(name = "Rajesh", surname = "patil")
print_kargs(name = "jayant")