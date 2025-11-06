'''Input: x = 2, n = 3
Output: 8
Explanation: 
2^3 = 2 × 2 × 2 = 8
'''
def myPow(x, n):
    # Step 1: Start with result = 1 because multiplying by 1 doesn't change value
    result = 1

    # Step 2: Store n in another variable, because we might need to change it
    power = n

    # Step 3: If exponent is negative, make it positive
    # Example: x = 2, n = -3  =>  convert to (1/x)^3
    if power < 0:
        x = 1 / x        # 2 becomes 1/2
        power = -power   # -3 becomes 3

    # Step 4: Multiply x by itself 'power' times
    # Example: if power = 3 → do result = x * x * x
    for i in range(power):
        result = result * x

    # Step 5: Return the final result
    return result


# --- Example usage ---
x = float(input("Enter base (x): "))   # Example input: 2
n = int(input("Enter exponent (n): ")) # Example input: 3

print("Result:", myPow(x, n))
'''Time ComplexityTime Complexity
O(n) — because we multiply n time
O(1) — space (uses only a few variables)'''
def myPow(x, n):
    # Step 1: Handle negative exponent
    # If n < 0, invert x and make n positive
    if n < 0:
        x = 1 / x
        n = -n

    # Step 2: Initialize result = 1
    result = 1

    # Step 3: Repeat while n > 0
    while n > 0:
        # If n is odd, multiply result by x once
        if n % 2 == 1:
            result = result * x
        
        # Step 4: Square x (x = x * x)
        x = x * x

        # Step 5: Divide n by 2 (integer division)
        n = n // 2

    # Step 6: Return the final answer
    return result


# --- Example usage ---
x = float(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))
print("Result:", myPow(x, n))
