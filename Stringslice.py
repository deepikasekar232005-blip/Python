def string_slicing_indexing():
    # Define a string
    str1 = "Hello, World!"

    # Indexing
    print("Indexing:")
    print("First character:", str1[0])  # H
    print("Last character:", str1[-1])  # !

    # Slicing
    print("\nSlicing:")
    print("First 5 characters:", str1[:5])  # Hello
    print("Last 6 characters:", str1[-6:])  # World!
    print("Characters from index 2 to 7:", str1[2:8])  # llo, W

    # Slicing with step
    print("\nSlicing with step:")
    print("Every 2nd character:", str1[::2])  # Hlo ol!
    print("Every 3rd character:", str1[::3])  # HlWl!

    # Reverse string
    print("\nReverse string:")
    print(str1[::-1])  # !dlroW ,olleH

# Run the function
string_slicing_indexing()
