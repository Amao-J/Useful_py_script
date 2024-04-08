import sys
import webbrowser

import pyperclip


address=''.join(sys.argv[1:]) if len(sys.argv) > 1 else pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')

print(address)