def caesar_cipher(message, key):

    result = ""

    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + key) % 26 + ord(
                'a' if char.islower() else 'A'))
            result += shifted_char
        else:
            result += char

    return result


message = input("Enter the message to encrypt: ")
key = int(input("Enter the encryption key: "))

encrypted_message = caesar_cipher(message, key)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", caesar_cipher(encrypted_message, -key))
