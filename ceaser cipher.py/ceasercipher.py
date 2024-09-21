from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(start_text,shift_amount,cipher_direction):
    final_txt = ""

    if shift < 1:
        print("Shift amount must be greater than 1")
        return
    
    #making option incase user selects decode we subtract the shift
    if cipher_direction.lower() == "decode":
            shift_amount *= -1
    
    for char in start_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos + shift_amount) % len(alphabet)
            new_letter = alphabet[new_pos]
        else:
         #preserve non alphabet letters
            new_letter = char
        final_txt += new_letter

    print(f'Your {cipher_direction}d text is {final_txt}.')
    decision = input("Do you want to keep encoding/decoding (yes or no): ")
    if decision.lower() == "yes":
        new_text = input("Type your message: ")
        new_shift = int(input("Enter the shift amount: "))
        new_direction = input("Type encode or decode: ")
        ceaser(start_text=new_text, shift_amount=new_shift, cipher_direction=new_direction)
    else:
        print("Thank you for using my Caesar Cipher program!")

        

ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)