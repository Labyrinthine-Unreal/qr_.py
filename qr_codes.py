import qrcode 
qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
) 

qr.add_data('https://foundation.app/@makemamaproud/foundation/125752')
qr.make()

img = qr.make_image(fill_color="blue", back_color="#ffe4e1") 
img.save('mama.png')
