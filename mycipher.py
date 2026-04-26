
import sys

def char_shift(c, shift):
    base = ord('A')
    offset = ord(c) - base
    new_offset = (offset + shift) % 26
    return chr(base + new_offset)

def encode_message(message, shift):
    message = message.upper()
    encoded = []
    for character in message:
        if 'A' <= character <= 'Z':
            encoded.append(char_shift(character, shift))
    return "".join(encoded)

def print_blocks(encoded):
    for i in range(0, len(encoded), 50):
        line = encoded[i:i+50]
        blocks = [line[j:j+5] for j in range(0, len(line), 5)]
        print(" ".join(blocks))

def main():
    shift = int(sys.argv[1])
    message = ""
    for line in sys.stdin:
        message += line
    encoded = encode_message(message, shift)
    print_blocks(encoded)

if __name__ == "__main__":
    main()

