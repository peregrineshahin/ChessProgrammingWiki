import os
import re

def process_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to find and replace opening code tags without C++
    count = 0
    def replace(match):
        nonlocal count
        count += 1
        if count % 2 == 1:  # Change only odd occurrences
            return f'```C++{match.group(1)}```'
        else:
            return match.group(0)

    updated_content = re.sub(r'```(.*?)```', replace, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Processed: {file_path}")

def process_all_md_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            process_md_file(file_path)

if __name__ == "__main__":
    # Replace 'your_directory' with the path to the directory containing your Markdown files
    target_directory = 'your_directory'
    
    process_all_md_files(target_directory)
    print("Code block tags updated in odd occurrences in all Markdown files.")
