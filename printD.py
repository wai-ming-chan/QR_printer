import qrcode

# Data to be encoded (Ctrl+D is U+0004 in Unicode, followed by a newline character)
data = "\x04\n"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box where the QR code is drawn
    border=4,  # Thickness of the border (minimum is 4)
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("qr_code_ctrl_d_newline.png")

# To display the image inline (optional if running in a Jupyter notebook)
img.show()
