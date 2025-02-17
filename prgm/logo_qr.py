from PIL import Image
import qrcode


qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,
    border=4,
)


qr.add_data("https://robosocnith-6zzx.vercel.app/ ")
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white").convert('RGB')


logo = Image.open("logo.png")  
logo = logo.resize((50, 50))


pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)


img.save("custom_qr_with_logo.png")
