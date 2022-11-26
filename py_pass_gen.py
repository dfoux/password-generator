import pyperclip
import random

password_length = int(input("Desired length?"))

pass_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "|", '!', '"', '@', '#', '$', '%', '^', '&', '*',
              '(', ')', '=', '*', '€', '£']

password = ""

for x in range(password_length):
    password = password + random.choice(pass_chars)

    pyperclip.copy(password)
