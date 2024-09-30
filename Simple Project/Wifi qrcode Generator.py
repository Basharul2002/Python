# pip install wifi qrcode generator


from wifi_qrcode_generator import wifi_qrcode


qr_code = wifi_qrcode("Basharul Alam", hidden=False, authentication_type="WPA", password="Mazu2002")
qr_code_img = qr_code.make_image()
qr_code_img.save("wifi_qr_code.png")