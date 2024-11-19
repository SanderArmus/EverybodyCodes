filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q03_p1.txt'
with open(filename, 'r') as file:
    matrix = [list(line.strip()) for line in file if line.strip()]
count=0
count_plus=0
depth=1
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "#":
            matrix[r][c] = 1
            count_plus+=1
            count+=1
while count_plus!=0:
    new_count_plus = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (0 < r < len(matrix) - 1) and (0 < c < len(matrix[r]) - 1):
                if (((matrix[r][c] == depth) or matrix[r][c] ==depth+1)  and
                    ((matrix[r + 1][c] == depth) or (matrix[r+1][c] ==depth+1))and
                    ((matrix[r - 1][c] == depth) or (matrix[r-1][c] ==depth+1))and
                    ((matrix[r][c - 1] == depth) or (matrix[r][c-1] ==depth+1))and
                    ((matrix[r][c + 1] == depth) or (matrix[r][c+1] ==depth+1))):
                    matrix[r][c] = depth + 1
                    new_count_plus += 1
                    count+=1
    count_plus = new_count_plus
    depth += 1

print(count)

