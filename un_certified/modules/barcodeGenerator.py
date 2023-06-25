from barcode import EAN13

number = '46446164611561511515'
ean_code = EAN13(number)
ean_code.save('barcode')