"""Examples of unit testing and random serial generation."""

import random
import string
import unittest


class MyTestCase(unittest.TestCase):
    """Test basic Python values and comparisons."""

    def test_value_is_in_list(self) -> None:
        """Check that 10 exists in the list."""
        self.assertIn(10, [5, 7, 8, 10])

    def test_value_is_integer(self) -> None:
        """Check that 10 is an integer."""
        self.assertIsInstance(10, int)

    def test_number_is_truthy(self) -> None:
        """Check that 100 evaluates to True."""
        self.assertTrue(bool(100))

    def test_empty_list_is_falsy(self) -> None:
        """Check that an empty list evaluates to False."""
        self.assertFalse(bool([]))

    def test_number_is_greater_or_equal(self) -> None:
        """Check that 100 is greater than or equal to 90."""
        self.assertGreaterEqual(100, 90)


###########################################


def generate_serial() -> str:
    """Generate a random serial containing three groups."""
    chars = string.ascii_letters + string.digits

    part1 = "".join(random.choices(chars, k=4))
    part2 = "".join(random.choices(chars, k=4))
    part3 = "".join(random.choices(chars, k=6))

    return f"{part1}-{part2}-{part3}"


if __name__ == "__main__":
    unittest.main(exit=False)
    print(generate_serial())
