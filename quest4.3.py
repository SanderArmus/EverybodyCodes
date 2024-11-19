filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q04_p3.txt'
numbers_list = []
kokku = 0

with open(filename, 'r') as file:
    for line in file:
        number = int(line.strip())
        numbers_list.append(number)

sorted_list = sorted(numbers_list)

n = len(sorted_list)
if n % 2 == 0:
    median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
else: 
    median = sorted_list[n // 2]

for number in numbers_list:
    if number <= median:
        kokku += median - number
    else:
        kokku += number - median

print(kokku)

