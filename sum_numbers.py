# Ask how many numbers to add
count = int(input("How many numbers do you want to add? "))

total = 0

# Collect and add each number
for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

print("The sum is:", total)
