import sys

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
    # Replace the incorrect import with the correct one.
    data = data.replace("from typing.io import TextIO", "from typing import TextIO")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"Fixed {filepath}")

if __name__ == '__main__':
    for file in sys.argv[1:]:
        fix_file(file)