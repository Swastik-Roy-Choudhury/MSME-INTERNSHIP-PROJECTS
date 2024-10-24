def caesar_cipher(text, shift):
    """Encrypts or decrypts a text using the Caesar Cipher algorithm.

    Args:
        text: The text to be encrypted or decrypted.
        shift: The number of positions to shift the letters.

    Returns:
        The encrypted or decrypted text.
    """

    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def main():
    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Quit\n").strip()

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if choice == "3":
            break

        text = input("Enter the text: ").strip()
        shift = int(input("Enter the shift value: "))

        if choice == "1":
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, -shift)
            print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()