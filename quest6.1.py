filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q06_p1.txt'

# Initialize an empty dictionary
dictionary = {}

# Read data from the file and construct the dictionary
with open(filename, 'r') as f:
    data = f.read()  # Read the entire file content as a string
    for line in data.strip().split('\n'):
        # Split the line into key and values
        key, values = line.split(':')
        # Split the values by comma and strip any whitespace
        value_list = [value.strip() for value in values.split(',')]
        # Assign the list of values to the key in the dictionary
        dictionary[key.strip()] = value_list

# Function to search for all paths to '@'
def find_all_paths(keys, current_path, all_paths, path_lengths):
    for key in keys:
        # Add the current key to the path
        current_path.append(key)
        
        # Check if the current key has a value of '@'
        if '@' in dictionary[key]:  # Check if '@' is in the list of values
            all_paths.append(current_path.copy())  # Save the current path if found
            path_lengths.append(len(current_path))  # Save the length of the path
        
        # If the value is a list, check each value
        for value in dictionary[key]:
            if value in dictionary:  # Ensure the value is a key in the dictionary
                find_all_paths([value], current_path, all_paths, path_lengths)  # Recursively search
        
        current_path.pop()  # Remove the current key from the path after searching

# Start searching from keys in 'RR'
rr_keys = dictionary['RR']
all_paths = []  # List to store all paths to '@'
path_lengths = []  # List to store lengths of paths to '@'

# Find all paths starting from keys in RR
find_all_paths(rr_keys, [], all_paths, path_lengths)

# Find unique path lengths
length_count = {}
for length in path_lengths:
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1

# Collect unique paths
unique_paths = [path for path, length in zip(all_paths, path_lengths) if length_count[length] == 1]

# Output the result
print("All paths to '@':")
for path in all_paths:
    print(" -> ".join(path))

print("\nLengths of all paths to '@':")
print(path_lengths)

if unique_paths:
    print("\nUnique paths to '@':")
    for path in unique_paths:
        print(" -> ".join(path))
else:
    print("No unique paths to '@' found.")