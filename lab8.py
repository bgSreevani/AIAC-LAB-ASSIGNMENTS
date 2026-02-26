#Lab 8: Test-Driven Development with AI – Generating and Working with Test Cases
#Task Description #1 (Password Strength Validator – Apply AI in Security Context)
#• Task: Apply AI to generate at least 3 assert test cases for is_strong_password(password) and implement the validator function.
#• Requirements: o Password must have at least 8 characters. o Must include uppercase, lowercase, digit, and special character. o Must not contain spaces.
#Example Assert Test Cases: assert is_strong_password("Abcd@123") == True assert is_strong_password("abcd123") == False assert is_strong_password("ABCD@1234") == True
#Expected Output #1:• Password validation logic passing all AI-generated test cases.

import re

def is_strong_password(password: str) -> bool:
    # Must have at least 8 characters
    if len(password) < 8:
        return False
    
    # Must not contain spaces
    if " " in password:
        return False
    
    # Must include uppercase, lowercase, digit, and special character
    if not re.search(r"[A-Z]", password):  # Uppercase
        return False
    if not re.search(r"[a-z]", password):  # Lowercase
        return False
    if not re.search(r"[0-9]", password):  # Digit
        return False
    if not re.search(r"[^A-Za-z0-9]", password):  # Special character
        return False
    
    return True


# Valid strong passwords
assert is_strong_password("Abcd@123") == True   # Meets all requirements
assert is_strong_password("StrongPass!9") == True  # Longer, mixed characters
assert is_strong_password("Mix3d#Case") == True   # Mixed case, digit, special char

# Invalid passwords
assert is_strong_password("abcd123") == False    # Missing uppercase & special char
assert is_strong_password("ABCD1234") == False   # Missing lowercase & special char
assert is_strong_password("ABCD@1234") == False  # Missing lowercase
assert is_strong_password("Abcdefgh") == False   # Missing digit & special char
assert is_strong_password("Abcd@ 123") == False  # Contains space

print("All test cases passed ✅")





#Task Description #2 (Number Classification with Loops – Apply AI for Edge Case Handling)
#• Task: Use AI to generate at least 3 assert test cases for a classify_number(n) function. Implement using loops.
#• Requirements: o Classify numbers as Positive, Negative, or Zero. o Handle invalid inputs like strings and None. o Include boundary conditions (-1, 0, 1).
#Example Assert Test Cases: assert classify_number(10) == "Positive" assert classify_number(-5) == "Negative" assert classify_number(0) == "Zero"
#Expected Output #2: • Classification logic passing all assert tests.

def classify_number(n):
    # Handle invalid inputs
    if n is None or isinstance(n, str):
        return "Invalid Input"
    
    # Using loop to classify (though simple if-else works, requirement says use loops)
    for value in [n]:
        if value > 0:
            return "Positive"
        elif value < 0:
            return "Negative"
        else:
            return "Zero"

# Standard cases
assert classify_number(10) == "Positive"   # Positive number
assert classify_number(-5) == "Negative"   # Negative number
assert classify_number(0) == "Zero"        # Zero case

# Boundary conditions
assert classify_number(1) == "Positive"    # Smallest positive boundary
assert classify_number(-1) == "Negative"   # Smallest negative boundary

# Invalid inputs
assert classify_number("abc") == "Invalid Input"  # String input
assert classify_number(None) == "Invalid Input"   # None input
print("All test cases passed ✅")




#Task Description #3 (Anagram Checker – Apply AI for String Analysis)
#• Task: Use AI to generate at least 3 assert test cases formis_anagram(str1, str2) and implement the function.
#• Requirements: o Ignore case, spaces, and punctuation. o Handle edge cases (empty strings, identical words).
#Example Assert Test Cases: assert is_anagram("listen", "silent") == True assert is_anagram("hello", "world") == False assert is_anagram("Dormitory", "Dirty Room") == True
#Expected Output #3: • Function correctly identifying anagrams and passing all AI-generated tests.

import string
def is_anagram(str1: str, str2: str) -> bool:
    # Handle edge cases: empty strings
    if not str1 or not str2:
        return False
    
    # Normalize: lowercase, remove spaces and punctuation
    translator = str.maketrans('', '', string.punctuation + " ")
    clean_str1 = str1.lower().translate(translator)
    clean_str2 = str2.lower().translate(translator)
    
    # Compare sorted characters
    return sorted(clean_str1) == sorted(clean_str2)
# Standard cases
assert is_anagram("listen", "silent") == True   # Classic anagram
assert is_anagram("hello", "world") == False    # Not an anagram
assert is_anagram("Dormitory", "Dirty Room") == True  # Ignore case & spaces

# Edge cases
assert is_anagram("", "") == False              # Empty strings
assert is_anagram("Test", "Test") == True       # Identical words
assert is_anagram("A gentleman", "Elegant man") == True  # Ignore spaces & case
assert is_anagram("School master", "The classroom") == True  # Famous anagram
print("All test cases passed ✅")




#Task Description #4 (Inventory Class – Apply AI to Simulate Real- World Inventory System)
#• Task: Ask AI to generate at least 3 assert-based tests for an Inventory class with stock management.
#• Methods: o add_item(name, quantity) o remove_item(name, quantity) o get_stock(name)
#Example Assert Test Cases:
#inv = Inventory()
"""inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10
inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5
inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3"""
#Expected Output #4: • Fully functional class passing all assertions.


class Inventory:
    def __init__(self):
        # Dictionary to store items and their quantities
        self.stock = {}
    
    def add_item(self, name: str, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        # Add new item or update existing stock
        if name in self.stock:
            self.stock[name] += quantity
        else:
            self.stock[name] = quantity
    
    def remove_item(self, name: str, quantity: int):
        if name not in self.stock:
            raise ValueError(f"Item '{name}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.stock[name] < quantity:
            raise ValueError("Not enough stock to remove")
        self.stock[name] -= quantity
    
    def get_stock(self, name: str) -> int:
        return self.stock.get(name, 0)

# Example tests
inv = Inventory()
# Add items
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10
# Remove items
inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5
# Add another item
inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3
# Additional AI-generated tests
inv.add_item("Notebook", 7)
assert inv.get_stock("Notebook") == 7   # Newly added item
inv.add_item("Pen", 2)
assert inv.get_stock("Pen") == 7        # Updated quantity after adding more
try:
    inv.remove_item("Marker", 1)        # Removing non-existent item
except ValueError as e:
    assert str(e) == "Item 'Marker' not found in inventory"
try:
    inv.remove_item("Book", 5)          # Removing more than available
except ValueError as e:
    assert str(e) == "Not enough stock to remove"
print("All test cases passed ✅")




#Task Description #5 (Date Validation & Formatting – Apply AI for Data Validation)
#• Task: Use AI to generate at least 3 assert test cases for validate_and_format_date(date_str) to check and convert dates.
#• Requirements: o Validate "MM/DD/YYYY" format. o Handle invalid dates. o Convert valid dates to "YYYY-MM-DD".
#Example Assert Test Cases: assert validate_and_format_date("10/15/2023") == "2023-10-15" assert validate_and_format_date("02/30/2023") == "Invalid Date" assert validate_and_format_date("01/01/2024") == "2024-01-01"
#Expected Output #5: • Function passes all AI-generated assertions and handles edge cases.


from datetime import datetime
def validate_and_format_date(date_str: str) -> str:
    try:
        # Try parsing with strict MM/DD/YYYY format
        parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
        # Return formatted date as YYYY-MM-DD
        return parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        # If parsing fails, it's an invalid date
        return "Invalid Date"
# Valid dates
assert validate_and_format_date("10/15/2023") == "2023-10-15"  # Standard valid date
assert validate_and_format_date("01/01/2024") == "2024-01-01"  # New Year boundary
assert validate_and_format_date("12/31/2025") == "2025-12-31"  # End of year boundary

# Invalid dates
assert validate_and_format_date("02/30/2023") == "Invalid Date"  # February 30 doesn't exist
assert validate_and_format_date("13/01/2023") == "Invalid Date"  # Invalid month
assert validate_and_format_date("00/10/2023") == "Invalid Date"  # Invalid month zero
assert validate_and_format_date("11/31/2023") == "Invalid Date"  # November has only 30 days

# Edge cases
assert validate_and_format_date("02/29/2024") == "2024-02-29"  # Leap year valid date
assert validate_and_format_date("02/29/2023") == "Invalid Date"  # Non-leap year invalid date
print("All test cases passed ✅")





#for above codes of all 5 tasks,genrate doctest cases for each and every task to validate the functions and classes.
import doctest
def is_strong_password(password: str) -> bool:
    """
    Validates if the given password is strong based on specific criteria.

    Criteria:
    - Must have at least 8 characters.
    - Must include uppercase, lowercase, digit, and special character.
    - Must not contain spaces.

    >>> is_strong_password("Abcd@123")
    True
    >>> is_strong_password("abcd123")
    False
    >>> is_strong_password("ABCD@1234")
    False
    >>> is_strong_password("Abcdefgh")
    False
    >>> is_strong_password("Abcd@ 123")
    False
    """
    # Function implementation remains the same
    if len(password) < 8:
        return False
    if " " in password:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[^A-Za-z0-9]", password):
        return False
    return True
def classify_number(n):
    """
Classifies a number as Positive, Negative, or Zero.
    
    >>> classify_number(5)
    'Positive'
    >>> classify_number(-3)
    'Negative'
    >>> classify_number(0)
    'Zero'
    """
    if n is None or isinstance(n, str):
        return "Invalid Input"
    for value in [n]:
        if value > 0:
            return "Positive"
        elif value < 0:
            return "Negative"
        else:
            return "Zero"
def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if two strings are anagrams, ignoring case, spaces, and punctuation.

    >>> is_anagram("listen", "silent")
    True
    >>> is_anagram("hello", "world")
    False
    >>> is_anagram("Dormitory", "Dirty Room")
    True
    >>> is_anagram("", "")
    False
    >>> is_anagram("Test", "Test")
    True
    >>> is_anagram("A gentleman", "Elegant
    man")
    True
    >>> is_anagram("School master", "The classroom")
    True
    """
    translator = str.maketrans('', '', string.punctuation + " ")
    clean_str1 = str1.lower().translate(translator)
    clean_str2 = str2.lower().translate(translator)
    return sorted(clean_str1) == sorted(clean_str2)
class Inventory:
    """A simple inventory management class to add, remove, and check stock of items.
    >>> inv = Inventory()
    >>> inv.add_item("Pen", 10)
    >>> inv.get_stock("Pen")
    10
    >>> inv.remove_item("Pen", 5)
    >>> inv.get_stock("Pen")
    5
    >>> inv.add_item("Book", 3)
    >>> inv.get_stock("Book")
    3
    >>> inv.add_item("Notebook", 7)
    >>> inv.get_stock("Notebook")
    7
    >>> inv.add_item("Pen", 2)
    >>> inv.get_stock("Pen")
    7
    >>> inv.remove_item("Marker", 1)
    Traceback (most recent call last):
        ...
    ValueError: Item 'Marker' not found in inventory
    >>> inv.remove_item("Book", 5)
    Traceback (most recent call last):
        ...
    ValueError: Not enough stock to remove
    """
    def __init__(self):
        self.stock = {}
    
    def add_item(self, name: str, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if name in self.stock:
            self.stock[name] += quantity
        else:
            self.stock[name] = quantity
    
    def remove_item(self, name: str, quantity: int):
        if name not in self.stock:
            raise ValueError(f"Item '{name}' not found in inventory")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if self.stock[name] < quantity:
            raise ValueError("Not enough stock to remove")
        self.stock[name] -= quantity
    
    def get_stock(self, name: str) -> int:
        return self.stock.get(name, 0)
def validate_and_format_date(date_str: str) -> str:
    """
    Validates a date string in "MM/DD/YYYY" format and converts it to "YYYY-MM-DD" format.

    >>> validate_and_format_date("10/15/2023")
    '2023-10-15'
    >>> validate_and_format_date("02/30/2023")
    'Invalid Date'
    >>> validate_and_format_date("01/01/2024")
    '2024-01-01'
    >>> validate_and_format_date("02/29/2024")
    '2024-02-29'
    >>> validate_and_format_date("02/29/2023")
    'Invalid Date'
    """
    try:
        parsed_date = datetime.strptime(date_str, "%m/%d/%Y")
        return parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"
if __name__ == "__main__":
    doctest.testmod(verbose=True)







#Genarate unittest cases for each and every task to validate the functions and classes
import unittest
import re
import string
from datetime import datetime

class TestPasswordStrength(unittest.TestCase):
    """Tests for is_strong_password(password)"""

    def test_valid_password(self):
        self.assertTrue(is_strong_password("Abcd@123"))

    def test_missing_uppercase(self):
        self.assertFalse(is_strong_password("abcd@123"))

    def test_missing_lowercase(self):
        self.assertFalse(is_strong_password("ABCD@1234"))

    def test_missing_digit(self):
        self.assertFalse(is_strong_password("Abcdefgh"))

    def test_contains_space(self):
        self.assertFalse(is_strong_password("Abcd@ 123"))

class TestNumberClassification(unittest.TestCase):
    """Tests for classify_number(n)"""

    def test_positive_number(self):
        self.assertEqual(classify_number(10), "Positive")

    def test_negative_number(self):
        self.assertEqual(classify_number(-5), "Negative")

    def test_zero(self):
        self.assertEqual(classify_number(0), "Zero")

    def test_invalid_input_string(self):
        self.assertEqual(classify_number("abc"), "Invalid Input")

    def test_invalid_input_none(self):
        self.assertEqual(classify_number(None), "Invalid Input")
class TestAnagramChecker(unittest.TestCase):
    """Tests for is_anagram(str1, str2)"""

    def test_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_not_anagram(self):
        self.assertFalse(is_anagram("hello", "world"))

    def test_anagram_ignore_case_space(self):
        self.assertTrue(is_anagram("Dormitory", "Dirty Room"))

    def test_empty_strings(self):
        self.assertFalse(is_anagram("", ""))

    def test_identical_words(self):
        self.assertTrue(is_anagram("Test", "Test"))     
    def test_ignore_punctuation(self):
        self.assertTrue(is_anagram("A gentleman", "Elegant man"))
    def test_famous_anagram(self):
        self.assertTrue(is_anagram("School master", "The classroom"))
class TestInventory(unittest.TestCase): 
    """Tests for Inventory class"""

    def setUp(self):
        self.inv = Inventory()

    def test_add_item(self):
        self.inv.add_item("Pen", 10)
        self.assertEqual(self.inv.get_stock("Pen"), 10)

    def test_remove_item(self):
        self.inv.add_item("Pen", 10)
        self.inv.remove_item("Pen", 5)
        self.assertEqual(self.inv.get_stock("Pen"), 5)

    def test_get_stock_nonexistent_item(self):
        self.assertEqual(self.inv.get_stock("Nonexistent"), 0)

    def test_remove_nonexistent_item(self):
        with self.assertRaises(ValueError):
            self.inv.remove_item("Marker", 1)

    def test_remove_more_than_stock(self):
        self.inv.add_item("Book", 3)
        with self.assertRaises(ValueError):
            self.inv.remove_item("Book", 5)
    def test_add_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.inv.add_item("Pen", -5)
    def test_remove_negative_quantity(self):
        self.inv.add_item("Pen", 10)
        with self.assertRaises(ValueError):
            self.inv.remove_item("Pen", -3)
class TestDateValidation(unittest.TestCase):    
    """Tests for validate_and_format_date(date_str)"""

    def test_valid_date(self):
        self.assertEqual(validate_and_format_date("10/15/2023"), "2023-10-15")

    def test_invalid_date(self):
        self.assertEqual(validate_and_format_date("02/30/2023"), "Invalid Date")

    def test_leap_year_valid_date(self):
        self.assertEqual(validate_and_format_date("02/29/2024"), "2024-02-29")

    def test_leap_year_invalid_date(self):
        self.assertEqual(validate_and_format_date("02/29/2023"), "Invalid Date")
if __name__ == "__main__":    unittest.main()

#command to run the tests: python -m unittest lab8_1.py







#Geneate pytest cases for each and every task to validate the functions and classes
import pytest
def test_is_strong_password():
    assert is_strong_password("Abcd@123") == True
    assert is_strong_password("abcd123") == False
    assert is_strong_password("ABCD@1234") == False
    assert is_strong_password("Abcdefgh") == False
    assert is_strong_password("Abcd@ 123") == False
def test_classify_number():
    assert classify_number(10) == "Positive"
    assert classify_number(-5) == "Negative"
    assert classify_number(0) == "Zero"
    assert classify_number("abc") == "Invalid Input"
    assert classify_number(None) == "Invalid Input"
def test_is_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("Dormitory", "Dirty Room") == True
    assert is_anagram("", "") == False
    assert is_anagram("Test", "Test") == True
    assert is_anagram("A gentleman", "Elegant man") == True
    assert is_anagram("School master", "The classroom") == True
def test_inventory():
    inv = Inventory()
    inv.add_item("Pen", 10)
    assert inv.get_stock("Pen") == 10
    inv.remove_item("Pen", 5)
    assert inv.get_stock("Pen") == 5
    inv.add_item("Book", 3)
    assert inv.get_stock("Book") == 3
    with pytest.raises(ValueError):
        inv.remove_item("Marker", 1)
    with pytest.raises(ValueError):
        inv.remove_item("Book", 5)
    with pytest.raises(ValueError):
        inv.add_item("Pen", -5)
    with pytest.raises(ValueError):
        inv.remove_item("Pen", -3)
def test_validate_and_format_date():
    assert validate_and_format_date("10/15/2023") == "2023-10-15"
    assert validate_and_format_date("02/30/2023") == "Invalid Date"
    assert validate_and_format_date("01/01/2024") == "2024-01-01"
    assert validate_and_format_date("02/29/2024") == "2024-02-29"
    assert validate_and_format_date("02/29/2023") == "Invalid Date"
if __name__ == "__main__":
    pytest.main()

    
