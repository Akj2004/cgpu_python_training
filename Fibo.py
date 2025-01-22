def generate_fibonacci(n):
    """Generate a Fibonacci sequence with n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Start with the first two numbers
    sequence = [0, 1]

    # Generate the rest of the sequence
    for _ in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


# Input: Number of terms
try:
    num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if num_terms < 0:
        print("Please enter a positive integer.")
    else:
        result = generate_fibonacci(num_terms)
        print(f"Fibonacci sequence with {num_terms} terms: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
