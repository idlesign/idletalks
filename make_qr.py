#! /usr/bin/env python3
"""Creates qr.png in current directory, encoding text received from command line.

Requires "qrcode" and Pillow packages installed:
    > pip install qrcode Pillow

Usage to encode "some text":
    > ./make_qr.py some text

"""
from sys import argv
import qrcode


out_file = 'qr.png'
text = ' '.join(argv[1:])

print('Encoding "%s" as QR Code into "%s" ...' % (text, out_file))

qr = qrcode.QRCode(version=3, box_size=12, border=2)

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image()
img.save(out_file)

print('Done')
