filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q06_p3.txt'

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
def find_all_paths(keys, current_path, all_paths, path_lengths, visited):
    for key in keys:
        # Check if the key exists in the dictionary
        if key not in dictionary:
            print(f"Warning: '{key}' is not a valid key in the dictionary.")
            continue  # Skip this key if it doesn't exist
        
        # Check for cycles
        if key in visited:
            print(f"Cycle detected: '{key}' has already been visited.")
            continue  # Skip this key if it creates a cycle
        
        # Add the current key to the path and mark it as visited
        current_path.append(key)
        visited.add(key)
        
        # Check if the current key has a value of '@'
        if '@' in dictionary[key]:  # Check if '@' is in the list of values
            all_paths.append(current_path.copy())  # Save the current path if found
            path_lengths.append(len(current_path))  # Save the length of the path
        
        # If the value is a list, check each value
        for value in dictionary[key]:
            if value in dictionary:  # Ensure the value is a key in the dictionary
                find_all_paths([value], current_path, all_paths, path_lengths, visited)  # Recursively search
            else:
                print(f"Warning: '{value}' is not a valid key in the dictionary.")  # Handle invalid keys
        
        # Backtrack: remove the current key from the path and mark it as unvisited
        current_path.pop()
        visited.remove(key)

# Start searching from keys in 'RR'
rr_keys = dictionary.get('RR', [])  # Use .get() to avoid KeyError if 'RR' doesn't exist
all_paths = []  # List to store all paths to '@'
path_lengths = []  # List to store lengths of paths to '@'

# Find all paths starting from keys in RR
find_all_paths(rr_keys, [], all_paths, path_lengths, set())

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
    
    # Create a string from the first letters of keys in unique paths
    unique_path_first_letters = [''.join(key[0] for key in path) for path in unique_paths]
    print("\nStrings from first letters of unique paths:")
    for unique_path_string in unique_path_first_letters:
        print(unique_path_string)
else:
    print("No unique paths to '@' found.")

# Create a string from the first letter of each key in the dictionary
first_letters = ''.join(key[0] for key in dictionary.keys())
print("\nString of first letters of each key:", first_letters)
