import qrcode

img = qrcode.make("Hello World! This is Qrcode")
img.save("mycode.png")