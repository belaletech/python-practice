import cmath

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the two roots using the quadratic formula
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return root1, root2

# Get input from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Call the function to solve the quadratic equation
roots = solve_quadratic_equation(a, b, c)

# Display the roots
print("The roots of the quadratic equation are:", roots)
