def count_runic_symbols(text, runic_words):
    counted_positions = set()
    for word in runic_words:
        start = 0
        while start < len(text):
            start = text.find(word, start)
            if start == -1:
                break
            for i in range(len(word)):
                counted_positions.add(start + i)
            start += 1  
    return counted_positions
def count_symbols_both_directions(text, runic_words):
    counted_positions = count_runic_symbols(text, runic_words)
    reversed_text = text[::-1]
    reversed_positions = count_runic_symbols(reversed_text, runic_words)
    adjusted_reversed_positions = {len(text) - 1 - pos for pos in reversed_positions}
    all_positions = counted_positions | adjusted_reversed_positions   
    return len(all_positions)  
filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q02_p2.txt'
with open(filename, 'r') as file:
    content = file.readlines()
    words_line = content[0].strip()
    words_line = words_line[6:]  
    runic_words = words_line.split(',')
    runic_words = [word.strip() for word in runic_words]
    text = ''.join(content[2:])
total_runic_symbols = count_symbols_both_directions(text, runic_words)
print(f"Total number of runic symbols: {total_runic_symbols}")