from PIL import Image
filename = r'fav.png'
img = Image.open(filename)
img.save('logo.ico')
