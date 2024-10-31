# Step a) Create text files TF18_1 and TF18_2 with character strings of different lengths

try:
    print("Creating TF18_1.txt...")
    with open('TF18_1.txt', 'w') as file1:
        print("File TF18_1.txt was opened!")
        file1.write('This is the content of the first file.\nIt has multiple lines.\nThe end.')
        print("Content was written to TF18_1.txt!")
except IOError:
    print("Error: Could not create or write to TF18_1.txt")
finally:
    print("File TF18_1.txt was closed!")

try:
    print("Creating TF18_2.txt...")
    with open('TF18_2.txt', 'w') as file2:
        print("File TF18_2.txt was opened!")
        file2.write('Second file has different content, longer than the first one.\nIt also has multiple lines.\nThe conclusion is here.')
        print("Content was written to TF18_2.txt!")
except IOError:
    print("Error: Could not create or write to TF18_2.txt")
finally:
    print("File TF18_2.txt was closed!")

# Step b) Swap the contents of TF18_1 and TF18_2 using TF18_3, writing 20 characters per line into TF18_2

def read_full_content(filename):
    print(f"Reading content from {filename}...")
    try:
        with open(filename, 'r') as f:
            print(f"File {filename} was opened for reading!")
            content = f.read()
            print(f"Content read from {filename}!")
            return content
    except IOError:
        print(f"Error: Could not read {filename}")
        return ''
    finally:
        print(f"File {filename} was closed after reading!")

def write_content(filename, content):
    print(f"Writing content to {filename}...")
    try:
        with open(filename, 'w') as f:
            print(f"File {filename} was opened for writing!")
            f.write(content)
            print(f"Content was written to {filename}!")
    except IOError:
        print(f"Error: Could not write to {filename}")
    finally:
        print(f"File {filename} was closed after writing!")

def write_content_in_chunks(filename, content):
    print(f"Writing content to {filename} in chunks of 20 characters...")
    try:
        with open(filename, 'w') as f:
            print(f"File {filename} was opened for writing!")
            # Remove existing newlines to ensure lines have exactly 20 characters
            content_no_newlines = content.replace('\n', '')
            for i in range(0, len(content_no_newlines), 20):
                chunk = content_no_newlines[i:i+20]
                f.write(chunk + '\n')
                print(f"Wrote chunk to {filename}: {chunk}")
            print(f"Content was written to {filename} in chunks!")
        print(f"File {filename} was closed after writing!")
    except IOError:
        print(f"Error: Could not write to {filename}")

# Read contents of TF18_1 and TF18_2
content1 = read_full_content('TF18_1.txt')  # Original content of TF18_1
content2 = read_full_content('TF18_2.txt')  # Original content of TF18_2

# Write content1 to TF18_3.txt (as a backup)
write_content('TF18_3.txt', content1)

# Write content2 to TF18_1.txt (swap content2 into TF18_1 as is)
write_content('TF18_1.txt', content2)

# Read content from TF18_3.txt (original content of TF18_1)
content_temp = read_full_content('TF18_3.txt')

# Write content_temp to TF18_2.txt in 20-character chunks (swap content1 into TF18_2 with formatting)
write_content_in_chunks('TF18_2.txt', content_temp)

# Step c) Read contents of TF18_1 and TF18_2 and print them line by line

def print_file_contents(filename):
    print(f"Contents of {filename}:")
    try:
        with open(filename, 'r') as f:
            print(f"File {filename} was opened for reading!")
            for line in f:
                print(line.rstrip())
    except IOError:
        print(f"Error: Could not read {filename}")
    finally:
        print(f"File {filename} was closed after reading!")

print_file_contents('TF18_1.txt')
print_file_contents('TF18_2.txt')
