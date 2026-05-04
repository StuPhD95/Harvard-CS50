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

```python
"""
=  (assignment, copying right-to-left)
== (equality, comparing left and right)
!= (not equal to)
"""
x = int(input("What's x? "))
y = int(input("What's y? "))

#%%
if x < y:
    print("x is less than y")
elif x > y: # elif (else if)
    print("x is greater than y")
else:
    print("x is equal to y")

#%%
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#%%
if x == y :
    print("x is equal to y")
else:
    print("x is not equal to y")

#%%
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#%%
def main():
    n= int(input("n: "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def is_even_pythonic(n):
    return True if n%2 == 0 else False

def is_even_pythonic_best(n):
    return n%2 == 0

main()

#%%
name = input("What's your name? ")
 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Lecture 3 (Loops)**
