# Grammar Checker for Books

## Overview

This repository contains a Python script that checks the grammar of a book by dividing the content into logical sequences and utilizing the OpenAI ChatGPT model to check the grammar and structure of the text.

## Features

- **Grammar Checking**: The script utilizes the OpenAI ChatGPT model to check the grammar and structure of the text.
- **Dividing Content**: The book content is divided into logical sequences to facilitate efficient checking.
- **Customizable**: Users can adjust the script parameters to customize the checking process according to their requirements.

## Usage

1. **Clone Repository**:

   ```
   git clone https://github.com/lbehrndt/correcturer.git
   ```

2. **Install Dependencies**:

   ```
   pip install PyPDF2
   ```

3. **Run Script**:

   ```
   python grammar_checker.py book.txt
   ```

   Replace `book.txt` with the path to your book file.

## Example

Suppose you have a book file named `example_book.pdf`.  
- Add the book to the pdf_file directory

You can run the script as follows:

```
python main.py 
```

The script will process the book content, divide it into logical sequences, and check the grammar and structure using the ChatGPT model.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.