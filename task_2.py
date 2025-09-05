from collections import deque

def is_palindrome_deque(text):
    # Normalize the string: convert to lowercase and remove spaces
    normalized_text = "".join(char.lower() for char in text if char.isalnum())

    # Create a deque and add all characters
    char_deque = deque(normalized_text)

    # Compare characters from both ends
    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            return False
    return True

if __name__ == "__main__":
    # Test cases
    print(f"'racecar' is a palindrome: {is_palindrome_deque('racecar')}")
    print(f"'Racecar' is a palindrome: {is_palindrome_deque('Racecar')}")
    print(f"'A man, a plan, a canal: Panama' is a palindrome: {is_palindrome_deque('A man, a plan, a canal: Panama')}")
    print(f"'hello' is a palindrome: {is_palindrome_deque('hello')}")
    print(f"'madam' is a palindrome: {is_palindrome_deque('madam')}")
    print(f"'No lemon, no melon' is a palindrome: {is_palindrome_deque('No lemon, no melon')}")
    print(f"'Python' is a palindrome: {is_palindrome_deque('Python')}")
    print(f"'Was it a car or a cat I saw' is a palindrome: {is_palindrome_deque('Was it a car or a cat I saw')}")
