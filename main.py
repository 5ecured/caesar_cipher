alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
# user_text = input('Type your message:\n')
# user_shift = int(input('Type your shift number:\n'))

def encrypt(plain_text, shift_amount):
    encrypted_text = ''

    for letter in plain_text:
        position = 0
        position += (alphabet.index(letter) + shift_amount)

        if position > 25:
            position -= 26
            
        encrypted_text += alphabet[position]

    print(encrypted_text)

encrypt(shift_amount = 5, plain_text='hello')


def decrypt(plain_text, shift_amount):
    decrypted_text = ''

    for letter in plain_text:
        position = 0

        #not sure why unable to use "position -= alphabet.index(letter) - shift_amount", so must use temp
        temp = alphabet.index(letter) - shift_amount 

        position = temp

        decrypted_text += alphabet[position]

    print(decrypted_text)

decrypt(shift_amount=5, plain_text='mjqqt')