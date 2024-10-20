# Braille Converter

```markdown
This Python program converts input text into Braille using Unicode Braille patterns.

## Features

- Converts lowercase letters (a-z) and numbers (0-9) into Braille.
- Supports basic punctuation (comma, period, exclamation mark, etc.).
- Handles spaces between words.

## Requirements

- Python 3.x

## Usage

1. Download the `main.py` file.
2. Run the program using Python:
   ```bash
   python main.py
   ```
3. Enter the text you want to convert to Braille when prompted.

### Example
```bash
$ python main.py
Enter the text to convert to Braille: Hello, world!
Braille Conversion:
⠓⠑⠇⠇⠕⠂ ⠺⠕⠗⠇⠙⠖
```

### Supported Characters

- Letters: `a` to `z`
- Numbers: `0` to `9`
- Basic punctuation: `, . ! ? ( ) - ' / ; :`
- Space: Preserved between words.

## Customization

You can extend the `braille_dict` dictionary in the code to add more characters or symbols.

## License

This project is open-source and licensed under the [MIT License](LICENSE).

---

Feel free to contribute or suggest improvements!
