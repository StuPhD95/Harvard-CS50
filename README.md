# Harvard-CS50

**Lecture 1 Notes (Functions and Variables)**
```python
#%% Strings (str)
name = input("What's your name? ").strip().title()
first, last = name.split(" ")    # split at spaces
"""
.strip() removes left and right extra spaces from str
.capitalise() capitalises first word of str
.title() capitalises every word of str 
.split() splits str into multiple substrings
"""
print("Hello, " + first + " " + last)     # concatenation (+ " " +  to include space)
print("Hello,", first)
print("Hello, ", end="")     # named parameter of print (end="\n" by deafult)
print(first)
print(f"Hello, {first}")     # f-string

#%% Integers (int)
x = int(input("Choose x. ")) 
y = int(input("Choose y. "))
"""
Without int(), x+y would be the concatenation of x and y since input() returns a str.
"""
print(x+y)

#%% Floats (float)
x = float(input("What is x? "))
y = float(input("What is y? "))
print(round(x+y))      # round(#) rounds # to the nearest integer
print(f"{x+y:,}")      # :, formats the str with a comma each triple of digits with a comma
print(round(x/y,2))    # round(#,n) rounds # to n digits
print(f"{x+y:.2f}")    # .2f rounds to two digits

#%% Functions
name = input("What is your name? ")
def hello(person):
    print("Hello", person)
hello(name)

n = int(input("What is n? "))
def square(n):
    return n**2 # equivalent to pow(n,2)
square(n)
```

**Lecture 2 Notes (Conditionals)**
