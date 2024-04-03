import re

def remove_braces(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Remove everything between curly braces using regular expressions
    modified_content = re.sub(r'\{.*?\}', '', content, flags=re.DOTALL)

    with open(output_file, 'w') as f:
        f.write(modified_content)

# Usage example
input_file = 'baby-llama.cpp'
output_file = 'baby_llamba.txt'
remove_braces(input_file, output_file)
