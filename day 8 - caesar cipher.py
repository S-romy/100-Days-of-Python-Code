# TODO 1: Import and print the logo from art.py when the program starts.

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# TODO 2: What happens if the user enters a number/ symbol/ space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "encode":
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                output_text += alphabet[shift_position]
            if encode_or_decode == "decode":
                shift_position = alphabet.index(letter) - shift_amount
                shift_position %= len(alphabet)
                output_text += alphabet[shift_position]

    print(f"Here is your {encode_or_decode}d text: {output_text}")


# TODO 3: Can you figure out a way to restart the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    retry = input("Type 'yes' if you want to go again. Otherwise 'no':\n").lower()
    if retry == "no":
        should_continue = False
        print("Try again soon!")
