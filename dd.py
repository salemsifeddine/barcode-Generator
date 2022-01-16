import barcode
from barcode.writer import ImageWriter
from barcode import generate

print(barcode.PROVIDED_BARCODES)
EAN = barcode.get_barcode_class('code128')
ean = EAN('5901234123457')
fullname = ean.save('ean13_barcode')
ean = EAN('5901234123457', writer=ImageWriter())

f = open('new_code.svg', 'wb')
ean.write(f)

name = generate('code128', '5901234123457', output='barcode_svg')
generate('code128', '5901234123457', writer=ImageWriter(), output='barcode')

