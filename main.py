import qrcode
import os

def generate_qr(data, filename="qrcode.png", size=10, border=4, fill_color="black", back_color="white"):

    # check if the file already exists
    if os.path.exists(filename):
        print(f"warning! the file {filename} already exists. it will be overwritten.")

    try:
        # create a QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # generate the QR code image
        img = qr.make_image(fill=fill_color, back_color=back_color)
        
        # save the image
        img.save(filename)
        print(f"QR code successfully saved to {filename}")
    
    except Exception as e:
        print(f"error generating QR code: {e}")

# example usage
if __name__ == "__main__":
    text = input("enter text or a link for the QR code: ")
    generate_qr(text)
