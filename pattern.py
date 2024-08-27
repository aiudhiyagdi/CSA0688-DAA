def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Number of rows
rows = 4
print_pattern(rows)
