import qrcode

data = input("Escribe los datos que quieres que contenga el QR: ")


img = qrcode.make(data)

nombre_archivo = f"D:/coding/Python/PythonLearn/MiniPythonProjects/qr/myqrcode.png"
img.save(nombre_archivo)

print("QR creado con éxito!")