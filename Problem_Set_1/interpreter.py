expression = input("What's your expression? ").strip()
x, y, z = expression.split(" ")

if y == "+":
    sol = float(int(x)+int(z))
    print(sol)
elif y == "-":
    sol = float(int(x)-int(z))
    print(sol)
elif y == "*":
    sol = float(int(x)*int(z))
    print(sol)
else:
    sol = float(int(x)/int(z))
    print(sol)