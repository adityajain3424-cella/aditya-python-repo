# Control Flow Basics in Python
# This program demonstrates if-else, loops, break, and continue
# Beginner-friendly example

# -------- IF / ELIF / ELSE --------
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

print()  # blank line for readability


# -------- FOR LOOP --------
print("For loop example:")
for i in range(1, 6):
    print("Number:", i)

print()


# -------- WHILE LOOP --------
print("While loop example:")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print()


# -------- BREAK & CONTINUE --------
print("Break and Continue example:")
for num in range(1, 11):

    if num == 5:
        continue  # skips number 5

    if num == 9:
        break  # stops the loop at 9

    print(num)

print("\nProgram execution completed.")
