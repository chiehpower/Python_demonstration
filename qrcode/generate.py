import qrcode
from PIL import Image
import requests
from io import BytesIO

txt = ['http://0.0.0.0:8501', 'chieh']
img = qrcode.make(txt)
img.save('qrcode.png')

# -----

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(txt)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black").convert('RGB')
img.save('qrcode-1.png')

# -----

response = requests.get('https://avatars.githubusercontent.com/u/32332200?v=4')
logo_display = Image.open(BytesIO(response.content))
logo_display.thumbnail((60, 60))

logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)
img.save("qrcode-2.png")