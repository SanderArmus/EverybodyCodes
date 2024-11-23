import numpy as np
filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q05_p1.txt'
with open(filename, 'r') as f:
    data = f.read()
matrix = []
for line in data.strip().split('\n'):
    row = []
    for value in line.split():
        row.append(int(value))
    matrix.append(row)
matrix = list(map(list, zip(*matrix)))
for line in matrix:
    print(line)
roundin = 0
round = 0
while round < 10:
    roundin=round
    while roundin >= (len(matrix)):
        roundin = roundin - len(matrix)
    element = matrix[roundin][0]   
    if roundin==(len(matrix)-1):
        if element > len(matrix[0]):
            matrix[roundin].pop(0)
            matrix[0].insert(-(element-len(matrix[0])), element)
        else:
            matrix[roundin].pop(0)
            matrix[0].insert(element - 1, element)
    else:
        if element > len(matrix[roundin+1]):
            matrix[roundin].pop(0)
            matrix[roundin + 1].insert(-(element-len(matrix[0])), element)
        else:
            matrix[roundin].pop(0)
            matrix[roundin + 1].insert(element - 1, element) 
    for line in matrix:
            print(line)   
    for row in matrix:
        print(row[0])
    round+=1
    print("round "+str(round))