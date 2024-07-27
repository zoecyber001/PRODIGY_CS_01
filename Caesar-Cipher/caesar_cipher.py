def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    :param text: The input text to be encrypted or decrypted.
    :param shift: The number of positions to shift each character.
    :param mode: 'encrypt' to encrypt, 'decrypt' to decrypt.
    :return: The encrypted or decrypted text.
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            ascii_offset = 65 if char.isupper() else 97  # ASCII value for 'A' or 'a'
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    
    return result

# Input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypting the message
encrypted_message = caesar_cipher(message, shift, mode='encrypt')
print("Encrypted message:", encrypted_message)

# Decrypting the message
decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
print("Decrypted message:", decrypted_message)
