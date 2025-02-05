import qrcode

create=qrcode.make("http://54.72.195.169/")
create.save('qr-code/third-qr.png','PNG')