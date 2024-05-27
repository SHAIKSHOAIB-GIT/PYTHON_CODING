alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(given_text, given_shift):
    encrypted_text=""
    for letter in given_text:
        position = alphabet.index(letter)
        new_position = position + given_shift
        new_letter = alphabet[new_position]
        encrypted_text +=new_letter
    print(f"encoded text : {encrypted_text}")



def decrypt(encr_text, encr_shift):
    decrypted_text=""
    for letter in encr_text:
        position = alphabet.index(letter)
        new_position = position - encr_shift
        new_letter = alphabet[new_position]
        decrypted_text +=new_letter
    print(f"decoded text : {decrypted_text}")



if direction == "encode":
    encrypt(given_text=text, given_shift=shift)
elif direction == "decode":
    decrypt(encr_text=text,encr_shift=shift)    

