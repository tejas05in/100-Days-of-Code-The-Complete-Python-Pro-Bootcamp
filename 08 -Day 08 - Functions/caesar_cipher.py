from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(text, shift):
#     encrypted_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         if new_position >= len(alphabet):
#             new_position = new_position - len(alphabet)
#         encrypted_text += alphabet[new_position]
#     print(f"The encoded text is {encrypted_text}")


# def decrypt(text, shift):
#     decrypted_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         if new_position < 0:
#             new_position = new_position + len(alphabet)
#         decrypted_text += alphabet[new_position]
#     print(f"The decoded text is {decrypted_text}")

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    final_text = ""
    for letter in text:
        if letter not in alphabet:
            final_text += letter
            continue
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
            if new_position >= len(alphabet):
                new_position = new_position - len(alphabet)
        elif direction == "decode":
            new_position = position - shift
            if new_position < 0:
                new_position = new_position + len(alphabet)
        final_text += alphabet[new_position]
    print(f"The {direction}d text is {final_text}")


print(logo)

restart = "yes"

while restart == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    # TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(text, shift, direction)
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
