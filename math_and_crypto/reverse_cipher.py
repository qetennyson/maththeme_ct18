cipher_text = '.daed era meht fo owt fi ,terces a peek nac eerhT'

def reverse_cipher(message):
    i = len(message) - 1
    translated = ''
    while i >= 0:
        translated += message[i]
        i -= 1

    return translated

reverse_cipher(cipher_text)

while True:
    user_msg = input("Enter text to encrypt or decrypt: ")
    if user_msg == 'stop':
        break
    else:
        cipher = reverse_cipher(user_msg)
        print(cipher)


