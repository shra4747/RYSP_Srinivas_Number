def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

def number_to_letter(number):
    return chr(number + ord('A'))


a = int(input("Enter affine a: "))
b = int(input("Enter affine b: "))
inv = int(pow(a, -1, 26))

#someone is spying on us
def encode(plain_text):
    return_text = ""
    for letter in plain_text:
        if letter == " ":
            return_text += " "
        else:
            return_text += number_to_letter(int((letter_to_number(letter)*a+b)%26))

    return (return_text)

def decode(cipher_text):
    return_text = ""
    for letter in cipher_text:
        if letter == " ":
            return_text += " "
        else:
            # pow(5, -1, 26) inverse of 5 and 26
            return_text += number_to_letter((((letter_to_number(letter)-b)*inv)%26))
    return (return_text)
    

encoded = encode(input("Enter plain text: "))
print("Encoded:", encoded.upper())


decoded = decode(input("Enter cipher text: ")) 
print("Decoded:", decoded.lower())
    
    
