# Read user input
hours = int(input())
minutes = int(input())

# Logic
minutes += 15

hours += minutes // 60
minutes %= 60

if hours >= 24:
    hours = 0

# Print output
print(f'{hours}:{minutes:02d}')
