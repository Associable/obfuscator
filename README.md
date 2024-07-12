# Python Obfuscator 🛡️

## Overview

The Python Obfuscator is a desktop application designed to obfuscate Python code, making it harder to read and reverse-engineer. Built using Python, Tkinter, and customtkinter, this tool provides a user-friendly interface to select and obfuscate your Python files. The obfuscation process includes encoding, scrambling, and optional compression to enhance security.

## Features ✨

- **Code Obfuscation:** Converts readable Python code into obfuscated code to protect your intellectual property.
- **Custom Encoding:** Utilizes a customizable encoding scheme for obfuscation.
- **Compression Option:** Optional compression of the obfuscated code for added security.
- **User-Friendly Interface:** Easy-to-use graphical interface with file browsing and obfuscation functionality.

## Prerequisites ⚙️

Ensure Python is installed on your system. This app depends on the following packages:

- `customtkinter`
- `tqdm`

Install the required packages using pip:

pip install customtkinter tqdm

## Installation 🔧

1. **Clone the Repository:**

    ```bash
    git clone <https://github.com/Associable/obfuscator>
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd idk ur project directory
    ```

3. **Install Required Packages:**

    ```bash
    pip install customtkinter tqdm
    ```

## Usage 🚀

1. **Run the Application:**

    ```bash
    python app.py
    ```

2. **Obfuscate Code:**

    - Click the "Browse" button to select a Python file.
    - The application will obfuscate the code and save the obfuscated version in the same directory with "(output)" appended to the filename.

## Code Breakdown 🔍

- **Obfuscate Code Function:** The core function that handles reading, obfuscating, and saving the code.
- **Custom Encoding Scheme:** Encodes characters using a base conversion method and optional compression.
- **User Interface:** Built with Tkinter and customtkinter for a modern, user-friendly experience.

## Credits 🤝

Special thanks to [@TheOnlyIcebear](https://github.com/TheOnlyIcebear) for creating the obfuscation part of this tool.

## Contributing 🤝

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details.
