import qrcode

data = 'darl\'a is darling but darling is not darla'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'pink', bacck_colour = 'blue')

img.save('C:/Users/91788/Documents/qrcode/myqrcode1.png')
