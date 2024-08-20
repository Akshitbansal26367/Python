# Prompt the user to enter the number of rows and columns
print("Enter number of rows and columns respectively : ", end="")

# Read the input values, split them by space, and convert them to integers
R, C = map(int, input().split(' '))

# Generate the upper part of the pattern
for i in range(1, R, 2):  # Loop starts at 1, increments by 2 (odd numbers only)
    # Generate the '.|.' pattern repeated 'i' times, then center it within 'C' columns with '-' filling the space
    print(('.|.' * i).center(C, '-'))

# Print the "WELCOME" text centered within 'C' columns, with '-' filling the space
print("WELCOME".center(C, '-'))

# Generate the lower part of the pattern
for i in range(R - 2, -1, -2):  # Loop starts at R-2 (second last line), decrements by 2 (odd numbers only)
    # Generate the '.|.' pattern repeated 'i' times, then center it within 'C' columns with '-' filling the space
    print(('.|.' * i).center(C, '-'))
