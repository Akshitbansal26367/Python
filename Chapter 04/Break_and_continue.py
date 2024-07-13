# Break statement is used to bring the control out of the loop when some external condition is triggered.
i = 1
while i <= 10:
    if i == 5:
        break
    print("Value of i =", i)
    i = i + 1

# When the continue statement is executed in the loop, the code inside the loop following the continue statement will
# be skipped for the current iteration and the next iteration of the loop will begin.
print()
a = 0
while a <= 10:
    a = a + 1
    if a == 5:
        continue
    print("Value of a = ", a)
