#Task1
def find_max(numbers):
    return max(numbers)

#Docstring Documentation with complete code
def find_max(numbers):
    """
    This function takes a list of numbers as input and returns the maximum value from the list.
    
    Parameters:
    numbers (list): A list of numerical values.
    
    Returns:
    The maximum value from the input list.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    
    # Use the built-in max function to find the maximum value in the list
    return max(numbers)
#Example usage
numbers = [3, 1, 4, 1, 5, 9]
max_value = find_max(numbers)
print(f"The maximum value in the list is: {max_value}")

#Inline Documentation with complete code
def find_max(numbers):
    """
    This function takes a list of numbers as input and returns the maximum value from the list.
    
    Parameters:
    numbers (list): A list of numerical values.
    
    Returns:
    The maximum value from the input list.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    
    # Use the built-in max function to find the maximum value in the list
    return max(numbers)
#Example usage
numbers = [3, 1, 4, 1, 5, 9]
max_value = find_max(numbers)
print(f"The maximum value in the list is: {max_value}")

#Google-Style Documentation with complete code
def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numerical values. The list should not be empty.   
    Returns:
        The maximum value from the input list.
    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    
    return max(numbers)
#Example usage
numbers = [3, 1, 4, 1, 5, 9]
max_value = find_max(numbers)
print(f"The maximum value in the list is: {max_value}") 

#Explanation of the code:
# The function `find_max` takes a list of numbers as input and returns the maximum value from that list. It first checks if the input list is empty and raises a ValueError if it is. If the list is not empty, it uses the built-in `max` function to find and return the maximum value. The function is documented using three different styles: docstring documentation, inline documentation, and Google-style documentation, providing clear explanations of the function's purpose, parameters, return value, and potential exceptions.      

#Task2
def login(user, password, credentials):
    return credentials.get(user) == password

#Docstring Documentation with complete code
def login(user, password, credentials):
    """
    This function checks if the provided username and password match the credentials stored in a dictionary.
    
    Parameters:
    user (str): The username to be checked.
    password (str): The password to be checked.
    credentials (dict): A dictionary containing username-password pairs.
    
    Returns:
    bool: True if the username and password match the credentials, False otherwise.
    """
    return credentials.get(user) == password
#Example usage
credentials = {'user1': 'pass1', 'user2': 'pass2'}
print(login('user1', 'pass1', credentials))  # Output: True
print(login('user1', 'wrongpass', credentials))  # Output: False

#Inline Documentation with complete code
def login(user, password, credentials):
    """
    This function checks if the provided username and password match the credentials stored in a dictionary.
    
    Parameters:
    user (str): The username to be checked.
    password (str): The password to be checked.
    credentials (dict): A dictionary containing username-password pairs.
    
    Returns:
    bool: True if the username and password match the credentials, False otherwise.
    """
    # Use the get method to retrieve the password for the given user and compare it with the provided password
    return credentials.get(user) == password
#Example usage
credentials = {'user1': 'pass1', 'user2': 'pass2'}
print(login('user1', 'pass1', credentials))  # Output: True
print(login('user1', 'wrongpass', credentials))  # Output: False

#Google-Style Documentation with complete code
def login(user, password, credentials):
    """
    Checks if the provided username and password match the credentials stored in a dictionary.

    Args:
        user (str): The username to be checked.
        password (str): The password to be checked.
        credentials (dict): A dictionary containing username-password pairs. The keys are usernames and the values are passwords. 
    Returns:
        bool: True if the username and password match the credentials, False otherwise. 
    """
    return credentials.get(user) == password
#Example usage
credentials = {'user1': 'pass1', 'user2': 'pass2'}
print(login('user1', 'pass1', credentials))  # Output: True
print(login('user1', 'wrongpass', credentials))  # Output: False

#Explanation of the code:
# The function `login` takes three parameters: `user`, `password`, and `credentials`. It checks if the provided username and password match the credentials stored in a dictionary. The function uses the `get` method of the dictionary to retrieve the password associated with the given username and compares it with the provided password. If they match, it returns `True`; otherwise, it returns `False`. The function is documented using three different styles: docstring documentation, inline documentation, and Google-style documentation, providing clear explanations of the function's purpose, parameters, return value, and potential exceptions.

#Task 3
#calculator.py 

#Task 4
#conversion.py

#Task 5
#course.py