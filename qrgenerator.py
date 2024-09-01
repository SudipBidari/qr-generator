import qrcode

def generate_qr_code(url, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image file
    img.save(filename)
    print(f"QR code for {url} saved as {filename}")

if __name__ == "__main__":
    # Example URL
    url = input("Enter the URL you want to encode into a QR code: ")
    filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")
    
    generate_qr_code(url, filename)
