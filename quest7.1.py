filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q07_p1.txt'
with open(filename, 'r') as f:
    data = f.read()

dictionary = {}
for line in data.strip().split('\n'):
    key, values = line.split(':', 1) 
    values = values.split(',') 
    dictionary[key.strip()] = [value.strip() for value in values] 
for key in dictionary.keys():
    while len(dictionary[key]) < 10:
        dictionary[key].extend(dictionary[key][:10 - len(dictionary[key])])  # Duplicate elements

all_answers = []

for key, row in dictionary.items():
    answer = 10 
    print(f"Processing {key}: {row}") 
    biganswer=10
    for element in row:
        print(f"Current element: '{element}'") 
        if element == "+":
            answer += 1
        elif element == "-":
            answer -= 1 
        elif element == "=":
            pass
        biganswer+=answer
        print(biganswer)
    all_answers.append({key: biganswer}) 
    print(f"Final answer for {key}: {biganswer}") 
print("All answers:", all_answers) 
combined_answers = {k: v for d in all_answers for k, v in d.items()}
sorted_dictionary = dict(sorted(combined_answers.items(), key=lambda item: item[1]))
print("".join(reversed(sorted_dictionary.keys())))