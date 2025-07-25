def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Interactive prompt
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
text = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

output = caesar_cipher(text, shift, mode)
print(f"Result: {output}")
