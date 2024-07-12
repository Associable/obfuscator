import random
import base64
import string
import names
import zlib
import math
import customtkinter as ctk
from tkinter import filedialog
from tqdm import tqdm

def obfuscate_code():
    recursion = 3
    base = 15000
    indent = 0
    bytes_allowed = True
    invisble_characters = False
    compress = False

    input_file = filedialog.askopenfilename(title="Select File to Obfuscate")

    if not input_file:
        return

    code = open(input_file, "rb").read().decode()

    if bytes_allowed:
        key = characters = list(map(chr, range(94, 94+base)))
    else:
        key = characters = list(map(chr, range(33, 34+base)))

    blacklist = ["'", "`", "\\"]

    for item in blacklist:
        if item in key:
            key.remove(item)
            base -= 1

    random.shuffle(key)
    highest = 0

    def encode(x, base):
        nonlocal highest
        if not x:
            return key[0]

        log = math.floor(math.log(x, base))

        st = [0]*(log+1)
        st[-1] = 1
        if log:
            x -= base**log

        while True:
            if x >= base:
                log = math.floor(math.log(x, base))
                x -= base**log
                st[log] += 1
                if st[log] > highest:
                    highest = st[log]
            else:
                st[0] = x
                if st[0] > highest:
                    highest = x
                return ''.join([str(key[char]) for char in st[::-1]])

    def decode(x, base):
        result = 0
        for count, char in enumerate(str(x)[::-1]):
            result += int(key.index(str(char)))*(base**count)

        return result

    for n in tqdm(range(recursion)):

        if n+1 == recursion:
            message = f"pass{'  '*indent};"
            if invisble_characters:
                base = 2
                key = ['​', '‍', '‎']
        else:
            message = ''
            random.shuffle(key)

        enc = '‌'.join([(str(encode(ord(chr), base))) for chr in code])
        enc2 = ' '.join([(str(encode(ord(chr), base))) for chr in 'exec'])
        enc3 = ' '.join([(str(encode(ord(chr), base))) for chr in 'compile'])
        src = f"""{message}lf1=lambda m: ''.join([ch[m**--++++0x0-1] for ch in '{''.join(key)}']);(eval(eval(''.join([chr(sum([lf1(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc2}'.split(' '))]), "", dir(__builtins__)[0x69-1])))(eval(''.join([chr(sum([lf1(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([lf1(++{base}**2).index(str(ch))*({hex(base)}**c) for c, ch in enumerate(str(x)[::-0x1])]))for x in('{enc}'.split('‌'))]), "", dir(__builtins__)[0x6a-1]))"""
        if compress:
            src = f'''eval(dir(__builtins__)[0x6a-1])(__import__('zlib').decompress(__import__('base64').b64decode(b'{base64.b64encode(zlib.compress(src.encode())).decode()}')).decode())'''

        print(len(enc), len(code), len(enc), len(src))
    output_file = f'{input_file} (output).py'
    with open(output_file, 'wb') as file:
        file.write(src.encode())

    print(f"Obfuscated code written to {output_file}")


def browse_file():
    obfuscate_code()

app = ctk.CTk()
app.geometry("400x200")
app.title("Python Obfuscator || Made By Lunar")

ctk.set_default_color_theme("dark-blue")

file_label = ctk.CTkLabel(app, text="")
file_label.pack(pady=20)

browse_button = ctk.CTkButton(app, text="Browse", command=browse_file)
browse_button.pack(pady=10)

app.mainloop()
