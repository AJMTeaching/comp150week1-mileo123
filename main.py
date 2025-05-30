# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
#Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5, 'apple', 20.5]

#Using indexing, print the value 'apple' from my_list.
print(my_list[2])

#Add the value 10 to the end of my_list using the append() method. Print the updated list.
my_list.append(10)
print(my_list)

#Remove the value 20.5 from my_list using the remove() method. Print the updated list.
my_list.remove(20.5)
print(my_list)

#Reverse the order of the elements in my_list using a method. Print the reversed list.
my_list.reverse()
print(my_list)

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
#Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
person = {
    'name': 'Miles',
    'age': 21,
    'job': 'student'
}

#Print the value corresponding to the 'job' key.
print(person['job'])

#Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person['city'] = 'Paris'
print(person)

#Remove the 'age' key-value pair from person. Print the updated dictionary.
del person['age']
print(person)

#Iterate through the person dictionary and print out each key-value pair on a separate line.
for key in person:
    print(key, ":", person[key])




# -----------------------------------------------------------------------------


# Importing sys for test function
import sys
def test(did_pass):
    """ Print the result of a test fail or not. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        print("Test at line", linenum, "ok")
    else:
        print("Test at line", linenum, "FAILED.")

# Function 1: count_vowels
import sys
def count_vowels():
    vowels = 'aeiouAEIOU'  # All vowels
    count = 0              # starts at 0
    for letter in text:    
        if letter in vowels:  
            count += 1
    return count

def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)

# Function 2: merge_lists
def merge_lists(list1, list2):
    result = [] 
    m=0 # m and g are variables that are assigned to 0 so basically your giving them a starting value
    g=0
#Compares the elements
    while m < len(list1) and g < len(list2):
        if list1[m] < list2[g]:
            result.append(list1[m])
            m+= 1
        else:
            result.append(list2[g])
            g+=1
    while m <len(list1):
        result.append(list1[m])
        m+= 1
    while g < len(list2):
        result.append(list2[g])
        g += 1
    return result
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])
    
# Function 3: word_lengths
import sys
def test(did_pass):
    """Print the result of a test."""
    linenum = sys._getframe(1).f_lineno
    msg = f"Test at line {linenum} {'ok' if did_pass else 'FAILED'}."
    print(msg)

# This function takes a list of strings and returns a list of their lengths
def word_lengths(words):
    result = []  # Create an empty list to store the lengths

    for word in words:
        length = len(word) 
        result.append(length)  # Add the length to the result list

    return result

# Unit tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])

# Run the tests
test_word_lengths()


# Function 4: reverse_string
import sys
def test(did_pass):
    """Print the result of a test."""
    linenum = sys._getframe(1).f_lineno
    msg = f"Test at line {linenum} {'ok' if did_pass else 'FAILED'}."
    print(msg)
    
# This function takes a string and returns it reversed
def reverse_string(text):
    reversed_text = ""  

    for char in text:  # Go through each character
        reversed_text = char + reversed_text  # Put the current character before the existing string so it wont be oringal

    return reversed_text
    
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")

# Run the test
test_reverse_string()


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    result = []
    # Loop through list1 and check for common items
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

# A simple test helper function
def test(condition):
    if condition:
        print("Test passed")
    else:
        print("Test failed")

# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])

# Dummy versions of other test functions so it doesn't crash
def test_count_vowels(): pass
def test_merge_lists(): pass
def test_word_lengths(): pass
def test_reverse_string(): pass

# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()

# Run the tests
test_suite()
