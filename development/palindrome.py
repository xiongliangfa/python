val = input("Enter a string to check if palindrome: ")
def palindrome(value):
    if value[::-1].lower() == value.lower():
        print("%s is palindrome" %value)
    else:
        print("%s is not palindrome" %value)
palindrome(val)
input("Press enter to close program")