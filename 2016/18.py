first_row = open("18.txt", "r").read().strip()

def is_next_trap(three):
    return three in ["^^.", ".^^", "^..", "..^"]

def next_row(row):
    next = ""
    row = '.' + row + '.'
    for i in range(1, len(row) - 1):
        if is_next_trap(row[i-1:i+2]):
            next += '^'
        else:
            next += '.'
    return next

# example
# row_ex = "..^^."
# print(row_ex)
# row_ex = next_row(row_ex)
# print(row_ex)
# row_ex = next_row(row_ex)
# print(row_ex)

# part 1
row = first_row
count = row.count('.')
for _ in range(39):
    row = next_row(row)
    count += row.count('.')
print(count)

# part 2
row = first_row
count = row.count('.')
for _ in range(399999):
    row = next_row(row)
    count += row.count('.')
print(count)
