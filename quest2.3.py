def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readline().strip().split(',')
            matrix = [list(line.strip()) for line in file if line.strip()]
        
        if not words or not matrix:
            raise ValueError("The input file is empty or improperly formatted.")
        
        return words, matrix
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def search_words_in_matrix(words, matrix):
    found_words = set()  
    positions = set()  

    rows = len(matrix)
    cols = len(matrix[0])


    def search_in_line(word, line, r, c, is_row=True):
        start_index = 0
        while start_index < len(line): 
            start_index = line.find(word, start_index)
            if start_index == -1:
                break

            for i in range(len(word)):
                if is_row:
                    positions.add((r, (start_index + i) % cols))
                else:
                    positions.add(((start_index + i) % rows, c))
            found_words.add(word)
            start_index += 1

    for word in words:
        for r in range(rows):
            row_str = ''.join(matrix[r])
            circular_row_str = row_str + row_str
            search_in_line(word, circular_row_str, r, 0, is_row=True)
            search_in_line(word[::-1], circular_row_str, r, 0, is_row=True)
        for c in range(cols):
            col_str = ''.join(matrix[r][c] for r in range(rows))
            search_in_line(word, col_str, 0, c, is_row=False)
            search_in_line(word[::-1], col_str, 0, c, is_row=False)

    return found_words, positions

def write_visual_matrix_to_file(visual_matrix, output_filename):
    with open(output_filename, 'w') as file:
        for row in visual_matrix:
            file.write(''.join(row) + '\n')

filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q02_p3.txt'  
try:
    words, matrix = read_input_file(filename)

    found, positions = search_words_in_matrix(words, matrix)

    visual_matrix = [['X' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for pos in positions:
        r, c = pos
        visual_matrix[r][c] = matrix[r][c].lower() 
    print(f"Found words: {', '.join(found)}")
    print("Visual Matrix of Found Characters:")
    for row in visual_matrix:
        print(''.join(row))

    print(f"Unique positions of found characters: {positions}")
    print(f"Total unique positions: {len(positions)}")

    output_filename = '/Users/sanderarmus/Kool/EverybodyCodes/visual_matrix.txt' 
    write_visual_matrix_to_file(visual_matrix, output_filename)
    print(f"Visual matrix written to {output_filename}")

except Exception as e:
    print(f"An error occurred during execution: {e}")
