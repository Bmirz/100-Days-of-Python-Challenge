alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  for letter in start_text:
    position = alphabet.index(letter)
    if cipher_direction == "encode":
      new_position = position + shift_amount
    elif cipher_direction == "decode":
      new_position = position - shift_amount
    end_text += alphabet[new_position]
  print(f"The text reads {end_text}")

  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
