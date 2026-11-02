"""Examples of Python modules, image processing, and functions."""

from pathlib import Path

from PIL import Image

# Zip Examples

# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#     my_data.append(data[0] + data[1])

# final_string = "".join(my_data).capitalize()

# print(final_string)  # Elzero

# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     if isinstance(item1, str):
#         my_data.append(item1)

# final_string = "".join(my_data).capitalize()
# print(final_string)  # Elzero


# Pillow Examples

image_path = Path(__file__).resolve().parent / "elzero-pillow.png"

if image_path.exists():
    with Image.open(image_path) as image:
        # Extract the L Letter
        l_box = (400, 0, 800, 400)

        l_image = image.crop(l_box)
        l_image = l_image.convert("L")

        l_output = image_path.with_name("elzero-pillow-L.png")
        l_image.save(l_output)

        # Extract the Second Row
        second_row_box = (0, 400, 1200, 800)

        second_row = image.crop(second_row_box)
        second_row = second_row.convert("L")
        second_row = second_row.rotate(180)

        second_output = image_path.with_name("elzero-pillow-L2.png")
        second_row.save(second_output)

    Image.open(l_output).show()
    Image.open(second_output).show()
    print("Both images saved successfully!")

else:
    print(f"Image not found: {image_path.name}")


# Function with Type Hints


def say_hello(people: list[str]) -> None:
    """Print a hello message for each person in the list."""
    for someone in people:
        print(f"Hello {someone}")


my_friends = ["Ahmed", "Osama", "Sayed"]

say_hello(my_friends)
