filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q04_p1.txt'
numbers_list = []
sum=0
with open(filename, 'r') as file:
    for line in file:
        number = int(line.strip())
        numbers_list.append(number)
smallest=min(numbers_list)
for number in numbers_list:
    sum+=number-smallest
print(sum)

