import qrcode

# Data to encode
data = "www.youtube.com/@sanjayyedage9652"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box
    border=4,  # border size (minimum 4)
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color='black', back_color='white')

# Save the image
img.save("qrcode_example.png")

# Display the image (opens default image viewer)
img.show()
