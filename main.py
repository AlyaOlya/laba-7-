from PIL import Image , ImageFilter

def z1():
    f = "sobaken.jpg"
    with Image.open(f) as t:
        img.load()

    img.show()
    height, width = img.size

    y = img.format

    u = img.mode

    print("Ширина: " , width)
    print("Высота: " , height)
    print("Формат: " , y)
    print("Цветовая модель: " , u)

def z2():
    i = Image.open('3.jpg')

    i1 = i.reduce(3)
    i1.save('3_1.jpg')

def z3():
    for i in range(1, 6):
        f = Image.open(str(i) + '.jpg')
        f = f.filter(ImageFilter.SHARPEN)
        f.save('z3_y' + str(i) + '.jpg')
        f.show()

def z4():
    i = Image.open("watermark.png")
    g = Image.open("1.ipg")

    g.paste(i, (50,50), i)

    g.save('v.jpg')
    g.show()


z1()
z2()
z3()
z4()