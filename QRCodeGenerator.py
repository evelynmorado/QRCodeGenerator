import qrcode

link = input("Enter a link: ")
img = qrcode.make(link)
name = input("Enter a name for the QR image: ")
img.save(name + ".png")
