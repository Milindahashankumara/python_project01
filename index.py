# Get input from the user
a = input("Enter value a = ");
b = input("Enter value b = ");

# Convert inputs to integers
a = int(a)
b = int(b)

# Swap values
a = a + b
b = a - b
a = a - b

# Print the swapped values
print("a =", a, '\n', "b =", b);
