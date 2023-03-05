import qrcode
import barcode_creation
# from barcode_creation import a
text = "http://127.0.0.1:5000"
qr_image = qrcode.make(text)
qr_image.save("new_qrcode.png")
