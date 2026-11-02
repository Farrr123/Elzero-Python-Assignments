import os
from pathlib import Path

# Use the current script directory for all file operations
folder = Path(__file__).resolve().parent


# Create files from txt1.txt to txt50.txt
for number in range(1, 51):
    if number == 25:
        special_file = folder / "special-text.txt"

        with special_file.open("w", encoding="utf-8"):
            pass

        continue

    file_path = folder / f"txt{number}.txt"

    with file_path.open("w", encoding="utf-8") as my_file:
        my_file.write(f"El zero Web School => {number}\n")

        if number == 1:
            my_file.write("Appended => Elzero Web School\n" * 50)


print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.path.basename(__file__))

files = os.listdir(folder)
print(len(files))

# Read txt1.txt and calculate its statistics
file_path = folder / "txt1.txt"

with file_path.open("r", encoding="utf-8") as my_file:
    content = my_file.read()

print(f"Number Of Lines Is => {len(content.splitlines())}")
print(f"Number Of Words Is => {len(content.split())}")
print(f"Number Of Chars Is => {len(content)}")
print(f'Number Of "l" Char Is => {content.count("l")}')

# Delete only txt41.txt to txt50.txt
for number in range(41, 51):
    file_path = folder / f"txt{number}.txt"

    if file_path.exists():
        os.remove(file_path)

#################################################

# DONE
