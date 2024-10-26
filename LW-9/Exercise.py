# Step a) Create text files TF18_1 and TF18_2 with character strings of different lengths

try:
    with open('TF18_1.txt', 'w') as file1:
        file1.write('This is the content of the first file.\nIt has multiple lines.\nThe end.')
except IOError:
    print("Error: Could not create or write to TF18_1.txt")

try:
    with open('TF18_2.txt', 'w') as file2:
        file2.write('Second file has different content, longer than the first one.\nIt also has multiple lines.\nThe conclusion is here.')
except IOError:
    print("Error: Could not create or write to TF18_2.txt")

# Step b) Swap the contents of TF18_1 and TF18_2 using TF18_3, writing 20 characters per line

def read_full_content(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError:
        print(f"Error: Could not read {filename}")
        return ''

def write_content_in_chunks(filename, content):
    try:
        with open(filename, 'w') as f:
            for i in range(0, len(content), 20):
                f.write(content[i:i+20] + '\n')
    except IOError:
        print(f"Error: Could not write to {filename}")

# Read contents of TF18_1 and TF18_2
content1 = read_full_content('TF18_1.txt')
content2 = read_full_content('TF18_2.txt')

# Write content1 to TF18_3.txt in chunks
write_content_in_chunks('TF18_3.txt', content1)

# Write content2 to TF18_1.txt in chunks
write_content_in_chunks('TF18_1.txt', content2)

# Read content from TF18_3.txt and write to TF18_2.txt
content_temp = read_full_content('TF18_3.txt')
write_content_in_chunks('TF18_2.txt', content_temp)

# Step c) Read contents of TF18_1 and TF18_2 and print line by line

def print_file_contents(filename):
    print(f"Contents of {filename}:")
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.rstrip())
    except IOError:
        print(f"Error: Could not read {filename}")

print_file_contents('TF18_1.txt')
print_file_contents('TF18_2.txt')
