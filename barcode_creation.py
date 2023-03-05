"""import barcode
from barcode import EAN13
from barcode.writer import SVGWriter, ImageWriter


# Or to an actual file:
with open("145.jpeg", "wb") as f:
    EAN13(str(100224554114), writer=SVGWriter()).write(f)

ean = barcode.get('ean13', '123456789123')
ean.get_fullcode()
filename = ean.save('ean13')
options = dict(compress=True)
filename = ean.save('ean13', options)

# ean = barcode.get('ean13', '100224554114', writer=ImageWriter())
# filename = ean.save('ean13_')"""

from io import BytesIO

from barcode import EAN13
from barcode.writer import ImageWriter

import random

a = random.randint(100000000000, 999999999999)

# Write to a file-like object:
rv = BytesIO()
EAN13(str(100000902922), writer=ImageWriter()).write(rv)

# Or to an actual file:
with open("parcel.jpeg", "wb") as f:
    EAN13(f"{a}", writer=ImageWriter()).write(f)
