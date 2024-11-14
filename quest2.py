import re
filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q02_p2.txt'
with open(filename, 'r') as file: 
    content = file.readlines()
    words = content[0]
    words = words[6:-1]
    words = words.split(',')
    text = ''.join(content[2:])
reversed_words = [word[::-1] for word in words]
for word in words:
    pattern = re.compile((word), re.IGNORECASE)
    text = pattern.sub(word.lower(), text)
for word in reversed_words:
    pattern = re.compile((word), re.IGNORECASE)
    text = pattern.sub(word.lower(), text)
print (text)
lowercase_count = sum(1 for char in text if char.islower())
print("Count of lowercase characters:", lowercase_count)