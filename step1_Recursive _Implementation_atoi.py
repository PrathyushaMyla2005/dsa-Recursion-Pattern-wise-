'''Problem Statement: Recursive Implementation of atoi()
💬 In simple words:
You are asked to convert a string of digits (for example "1234") into an integer (1234) — but without using loops or built-in functions like stoi() or atoi().
You must do it recursively — that means, the function should call itself to process each character one by one.
📖 What does atoi() mean?
🔹 atoi() = ASCII to Integer
It’s a standard C/C++ library function that converts a string containing digits into its integer value.
Example (built-in):int num = atoi("4567");  // num = 4567
'''
#brute force
'''Step 4: Plan the Steps (Before Writing Code)
Now that you know the logic, plan like this:
Take the input string.
Initialize a variable → result = 0.
For every character in the string:
Convert it to a number → digit = ord(char) - ord('0')
Add it into result using result = result * 10 + digit
If the number is negative, handle that.
Print the final result.'''
def atoi(s):
    result = 0

    for char in s:
        digit = ord(char) - ord('0')   # convert character to integer
        result = result * 10 + digit   # build the number step by step

    return result

# Example usage
print(atoi("1234"))  # Output: 1234
'''Time Complexity (TC): O(n)

Why?

The loop for char in s: runs once for each character in the string.

Inside the loop:

ord(char) → O(1)

Subtraction and multiplication → O(1)

So total work = n × O(1) = O(n)
✅ TC = O(n) where n is the number of digits in the string.

💾 Space Complexity (SC): O(1)

Why?

Uses only one variable result and a temporary digit.

No extra arrays, strings, or recursion calls.

✅ SC = O(1)'''
#when ask negative numbers
def atoi(s):
    # Step 1️⃣: Assume the number is positive initially
    negative = False

    # Step 2️⃣: Check if the number starts with '-'
    # If yes, mark it as negative and remove the first character '-'
    if s[0] == '-':
        negative = True
        s = s[1:]  # This skips the '-' sign (takes substring from index 1 to end)

    # Step 3️⃣: Initialize result to 0 (we will build the number step by step)
    result = 0

    # Step 4️⃣: Loop through each character in the string (e.g., '5', '6', '7', '8')
    for char in s:
        # Step 4.1: Convert character to its corresponding integer value
        # ord('0') = 48, ord('5') = 53, so ord('5') - ord('0') = 5
        digit = ord(char) - ord('0')

        # Step 4.2: Build the number by multiplying result by 10 and adding the digit
        # Example: result = 0 → 5 → 56 → 567 → 5678
        result = result * 10 + digit

    # Step 5️⃣: If the original string had a '-', make result negative
    if negative:
        result = -result

    # Step 6️⃣: Return the final integer result
    return result


# Step 7️⃣: Test the function
print(atoi("-5678"))  # Output: -5678
'''ep-by-Step Reasoning:

Checking the first character → O(1)

If negative, slicing s = s[1:] → O(n) (because slicing a string creates a new string)

Looping over each character → O(n)

Constant-time operations inside the loop (ord(), arithmetic) → O(1) each

➡️ Total Time Complexity = O(n) + O(n) = O(n)

✅ Final Time Complexity: O(n)
Where n = length of the string.

💾 Space Complexity (SC)
🔹 Step-by-Step Reasoning:

negative (boolean) → O(1)

result (integer) → O(1)

digit (integer) → O(1)

New substring created with s = s[1:] → O(n) (because it stores a copy of the string without the first character)

➡️ Total Space Complexity = O(n) (due to string slicing)

✅ Final Space Complexity: O(n)'''
def atoi_optimized(s):
    # Step 1: Handle empty input
    if not s:
        return 0

    # Step 2: Initialize variables
    result = 0
    negative = False
    start = 0  # start index for reading digits

    # Step 3: Check for negative or positive sign
    if s[0] == '-':
        negative = True
        start = 1  # skip first character
    elif s[0] == '+':
        start = 1  # just skip '+' sign

    # Step 4: Loop through characters from 'start' index
    for i in range(start, len(s)):
        char = s[i]

        # Check if the character is a digit
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
            result = result * 10 + digit
        else:
            # stop if a non-digit character appears
            break

    # Step 5: Apply sign if needed
    if negative:
        result = -result

    return result


# ✅ Example Test Cases
print(atoi_optimized("-5678"))  # ➡️ -5678
print(atoi_optimized("+1234"))  # ➡️ 1234
print(atoi_optimized("42"))     # ➡️ 42


'''The loop for i in range(start, len(s)):
iterates through each character exactly once.

Every operation inside (like ord(char) or arithmetic) takes constant time O(1).

So, total time =
👉 O(n) where n = length of the string.
e are only using a few fixed variables:

result, negative, start, char, digit


No extra data structures or new strings created.

Even if string size increases, these variables stay constant.
So, Space = Constant = O(1)'''