# Braille Converter

```markdown
This Python program converts input text and music notation into Braille using Unicode Braille patterns.

## Features

- Converts lowercase letters (a-z), numbers (0-9), and musical notes (C, D, E, F, G, A, B) into Braille.
- Supports basic punctuation (comma, period, exclamation mark, etc.).
- Handles musical symbols such as sharp, flat, natural, and notes (quarter note, eighth note).
- Asks the user whether to convert text or music notation.
- Provides an option to continue converting or exit the program after each conversion.

## Requirements

- Python 3.x

## Usage

1. Download the `main.py` file.
2. Run the program using Python:
   ```bash
   python main.py
   ```
3. Choose whether to convert text or music notation to Braille.
4. Enter the text or music notation you want to convert when prompted.

### Example

```bash
$ python main.py
What do you want to convert? (1) Text to Braille (2) Music Notation to Braille: 1
Enter the text to convert to Braille: Hello, world!
Braille Conversion:
⠓⠑⠇⠇⠕⠂ ⠺⠕⠗⠇⠙⠖
Do you want to continue? (yes to continue / no to exit): yes

What do you want to convert? (1) Text to Braille (2) Music Notation to Braille: 2
Enter the music notation to convert to Braille (e.g., C sharp, E flat): C sharp E flat
Braille Conversion:
⠉ ⠸ ⠑ ⠡
Do you want to continue? (yes to continue / no to exit): no
Exiting the program.
```

### Supported Characters

#### Text:
- Letters: `a` to `z`
- Numbers: `0` to `9`
- Basic punctuation: `, . ! ? ( ) - ' / ; :`
- Space: Preserved between words.

#### Music:
- Notes: `C, D, E, F, G, A, B`
- Symbols: Sharp (`sharp`), Flat (`flat`), Natural (`natural`)
- Notes: Quarter note (`quarter_note`), Eighth note (`eighth_note`)

## Customization

You can extend the `braille_dict` dictionary in the code to add more characters, symbols, or additional musical notation.

## License

This project is open-source and licensed under the [MIT License](LICENSE).

---

Feel free to contribute or suggest improvements!
