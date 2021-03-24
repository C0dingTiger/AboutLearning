
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# # String which represents the QR code 
# s = "https://adverpost.com"
  
# # Generate QR code 
# url = pyqrcode.create(s) 
  
# # Create and save the svg file naming "myqr.svg" 
# url.svg("myqr.svg", scale = 8) 
  
# # Create and save the png file naming "myqr.png" 
# url.png('myqr.png', scale = 6) 



import qrcode
from PIL import Image



qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://adverpost.com')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("sample.png")

