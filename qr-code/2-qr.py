import qrcode
from PIL import Image

myqr=qrcode.make("ec2-18-61-74-227.ap-south-2.compute.amazonaws.com")
myqr.save('second-qr.png','PNG')

o=Image.open('second-qr.png')
o.show()