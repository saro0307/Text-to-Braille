# Define a dictionary for Braille pattern Unicode values including music notation
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑', '6': '⠋',
    '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚', ' ': ' ', ',': '⠂', ';': '⠆', ':': '⠒',
    '.': '⠲', '!': '⠖', '?': '⠦', '(': '⠶', ')': '⠶', '-': '⠤', "'": '⠄', '/': '⠌',

    # Music notes
    'C': '⠉', 'D': '⠙', 'E': '⠑', 'F': '⠋', 'G': '⠛', 'A': '⠁', 'B': '⠃',
    
    # Other music symbols
    'sharp': '⠸',  # Sharp sign
    'flat': '⠡',   # Flat sign
    'natural': '⠷', # Natural sign
    'quarter_note': '⠈', # Quarter note
    'eighth_note': '⠘',  # Eighth note
    'repeat_sign': '⠦⠦'  # Repeat sign
}

def text_to_braille(text):
    # Convert input text (normal text or music notation) to Braille
    braille_output = []
    for word in text.split():
        if word in braille_dict:
            braille_output.append(braille_dict[word])
        else:
            braille_output.append(''.join([braille_dict.get(char.lower(), '') for char in word]))
    
    return ' '.join(braille_output)

# Main logic to ask the user what they want to convert
def main():
    while True:
        choice = input("What do you want to convert? (1) Text to Braille (2) Music Notation to Braille: ")

        if choice == '1':
            input_text = input("Enter the text to convert to Braille: ")
        elif choice == '2':
            input_text = input("Enter the music notation to convert to Braille (e.g., C sharp, E flat): ")
        else:
            print("Invalid choice. Please choose 1 or 2.")
            continue
        
        braille_text = text_to_braille(input_text)
        print("Braille Conversion:")
        print(braille_text)

        # Ask if the user wants to continue or exit
        cont = input("Do you want to continue? (yes to continue / no to exit): ").lower()
        if cont != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
