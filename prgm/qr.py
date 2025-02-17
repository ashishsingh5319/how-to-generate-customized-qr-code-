# how to generate qr code 
import qrcode 
from PIL import Image
import qrcode.compat
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=4,)

qr.add_data("https://robosocnith-6zzx.vercel.app/ ")
img=qr.make_image(fill_color="red",back_color="white")
img.save("robo_web.png")