def text_to_binary(text):
    binary_code = ""
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(8)  # Convert character to binary
        binary_code += binary_char + " "  # Add space between binary characters
    return binary_code.strip()  # Remove trailing space


def main():
    text = input("Enter the text to translate to binary: ")
    binary_text = text_to_binary(text)
    print("Binary code:", binary_text)


print("Made by Mohammed Azhaan Pasha")
print("Type one word at once for better results. Thank you!! Enjoy!!")
print("")

if __name__ == "__main__":
    main()
