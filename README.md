# Text Encryption and Decryption Using Matrix Rotation and Key Encoding

## Overview
This project implements text encryption and decryption using matrix-based character rotation and key encoding. The program allows users to encrypt and decrypt messages by aligning each letter of the text with a key and utilizing a rotating alphabet matrix.

## Features
- **Right Rotation of List Elements**: Rotates a list to the right by one position or by a user-specified number of steps.
- **Customizable Rotation Step**: The user can input a custom step value for list rotations.
- **Key-Based Text Encoding**: A method that encodes text using a key, repeating the key as needed.
- **Alphabet Matrix Construction**: Generates a 26x26 matrix where each row is a right rotation of the alphabet. This matrix is used for encoding and decoding.
- **Text Encryption**: Encrypts a message using the key and the alphabet matrix.
- **Text Decryption**: Decrypts a message using the same key and matrix.
- **User Interface**: Interactive prompts allow the user to choose between encryption and decryption and input their text and key.

## Usage

### Prerequisites
- Python 3.x

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/encryption-decryption-matrix-key.git
   cd encryption-decryption-matrix-key


2. Run the script:
   ```bash
   python encryption_decryption.py
   ```

3. Follow the interactive prompts:
   - Choose whether to encrypt or decrypt a message.
   - Enter the text to be encrypted or decrypted.
   - Provide a key (without spaces) for the encryption/decryption process.

## Example

### **Encryption**:
- **Text**: `"bonjour le monde"`
- **Key**: `"ntic"`
- **Encrypted Text**: `"nticnti cn ticnt"`

### **Decryption**:
- **Encrypted Text**: `"nticnti cn ticnt"`
- **Key**: `"ntic"`
- **Decrypted Text**: `"bonjour le monde"`

## Functions

### `rotation_droite(lst)`
Rotates the elements of a list to the right by one position.

### `texte_cle(txt, cle)`
Encodes the given text using a repeating key.

### `matrix_building(lst)`
Builds a 26x26 matrix where each row is a right rotation of the alphabet.

### `crypted_text_building(txt, txt_cle)`
Encrypts the text using the alphabet matrix and key.

### `decrypted_coded_text_building(ctxt, txt_cle)`
Decrypts the text using the alphabet matrix and key.

## Future Enhancements
- Add support for symbols and numbers.
- Add a graphical user interface (GUI) for better user experience.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.




