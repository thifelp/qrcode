import qrcode

data = 'Veja \n https://www.alura.com.br/artigos/pycharm-vscode-programar-python'

qr = qrcode.QRCode(version= 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'black', back_color = 'white')

path = '/home/thi/Pictures/test1.png'
img.save(path)
