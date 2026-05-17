# Caesar Cipher - Python CLI Project

## Overview
This project implements a simple Caesar Cipher encryption and decryption program in Python. The assignment focused on using the Unix command line interface (CLI), the `vi` editor, git, and GitHub rather than an IDE.

The program accepts a shift value through command-line arguments and encrypts/decrypts a one-line message entered through standard input.

For this repository, a shift value of **3** was used. The repo also includes:

- Original plaintext input file
- Encrypted output file
- Decrypted text file
- Python source code

---

## Technologies Used

- Python 3
- Unix/Linux CLI
- Git & GitHub
- vi Editor

---

## Features

- Caesar Cipher encryption
- Caesar Cipher decryption
- Uses command-line arguments (`sys.argv`)
- Reads user input from standard input
- Handles alphabet shifting using ASCII arithmetic
- Includes sample input/output files

---

## Files Included

| File | Description |
|------|-------------|
| `mycipher.py` | Main Python source code |
| `plaintext` | Original plaintext message |
| `cryptedtext` | Message encrypted with a shift of 3 |
| `newplaintext` | Decrypted message after reversing the shift |
| `README.md` | Project documentation |

---

## How It Works

A Caesar Cipher shifts each letter in the alphabet by a fixed number.

Example with a shift of 3:

- A → D
- B → E
- X → A
- Y → B
- Z → C

The program uses ASCII values and wraparound logic to correctly shift letters past `Z` or `z`.

---

## Running the Program

### Encrypt a Message

```bash
python3 mycipher.py 3
```

Then type your message and press Enter.

### Example

```bash
$ python3 mycipher.py 3
hello world
khoor zruog
```

---

## Decryption

To decrypt, use the reverse shift:

```bash
python3 mycipher.py 23
```

Since:

```text
26 - 3 = 23
```

---

## GitHub Workflow Used

This assignment was managed using git and GitHub from the command line.

Common commands used:

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

---

## Assignment Objectives

This project provided practice with:

- Writing code using `vi`
- Running programs from the Unix CLI
- Managing code with git
- Publishing repositories to GitHub
- Understanding basic cryptography concepts

---

## Author

Amaia M.
