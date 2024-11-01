def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    text = input("Введите текст: ")
    shift = int(input("Введите сдвиг: "))
    encrypted_text = caesar_encrypt(text, shift)
    print("Зашифрованный текст:", encrypted_text)
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Дешифрованный текст:", decrypted_text)
