# Define a dictionary for Braille pattern Unicode values
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑', '6': '⠋',
    '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚', ' ': ' ', ',': '⠂', ';': '⠆', ':': '⠒',
    '.': '⠲', '!': '⠖', '?': '⠦', '(': '⠶', ')': '⠶', '-': '⠤', "'": '⠄', '/': '⠌'
}

def text_to_braille(text):
    # Convert each character to Braille using the dictionary
    braille_output = ''.join([braille_dict.get(char.lower(), '') for char in text])
    return braille_output

# Input text from the user
input_text = input("Enter the text to convert to Braille: ")

# Convert and print the Braille equivalent
braille_text = text_to_braille(input_text)
print("Braille Conversion:")
print(braille_text)
