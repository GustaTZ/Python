import qrcode

#Link / Texto
link = 'https://www.youtube.com/@guzerasz'

img = qrcode.make(link)

#Diretorio de salvamento
img.save("C:/Users/546692668/Downloads/Teste/qrcodeteste1.png")