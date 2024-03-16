from PIL import Image
import qrcode

img=qrcode.make('https://docs.python.org/3/')

img.save('first-qr.png','PNG',scale=10)

o=Image.open("first-qr.png")
o.show()
