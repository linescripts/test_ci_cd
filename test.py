"""
Sample Python code with various issues to test a code reviewer bot.
"""

import os, sys  # Unused import "sys"

PASSWORD = "supersecret"  # Hardcoded password (bad practice)

def do_something():
    """
    This function does something—but not really.
    It also has some style issues intentionally left in for testing.
    """

    numbers = [1,2,3,4,5] 
    squares = []
    for i in range(len(numbers)):   # Should use enumerate
       squares.append(numbers[i]*numbers[i])

    if squares:
      print("We have squares!")  # inconsistent indentation

def read_file(filepath):
    """
    Reads and prints content of the file but doesn't handle exceptions properly.
    """
    f = open(filepath, 'r')    # Not using a context manager
    content = f.read()
    print(content)
    f.close()

def main():
    do_something()

    # This while loop never ends if user doesn't type "exit"
    while True:
        user_input = input("Type something (or 'exit'): ")
        if user_input.lower() == "exit":
            break
        print("You typed:", user_input)

if __name__ == "__main__":
    main()
