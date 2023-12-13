from os import walk
import random

from PIL import Image

filenames = next(walk("C:\\Users\\1\\PycharmProjects\\emoji\\result2"), (None, None, []))[2]  # [] if no file
print(filenames)
random.shuffle(filenames)
print(filenames)

w, h = 732, 732
sw, sh = 348, 348
num = 0
while len(filenames) > 0:
    num+=1
    with Image.open("main_bg.jpg") as img:
        with Image.open("C:\\Users\\1\\PycharmProjects\\emoji\\result2\\" + filenames[0]) as em:
            wbg = Image.new(mode="RGB", size=(sw, sh), color=(255, 255, 255))
            img.paste(wbg, (18, 18))
            em = em.convert("RGBA")
            new_em = em.resize((sw, sh))
            img.paste(new_em, (18, 18), new_em)

        with Image.open("C:\\Users\\1\\PycharmProjects\\emoji\\result2\\" + filenames[1]) as em:
            wbg = Image.new(mode="RGB", size=(sw, sh), color=(255, 255, 255))
            img.paste(wbg, (400, 18))
            em = em.convert("RGBA")
            new_em = em.resize((sw, sh))
            img.paste(new_em, (400, 18), new_em)

        with Image.open("C:\\Users\\1\\PycharmProjects\\emoji\\result2\\" + filenames[2]) as em:
            wbg = Image.new(mode="RGB", size=(sw, sh), color=(255, 255, 255))
            img.paste(wbg, (18, 400))
            em = em.convert("RGBA")
            new_em = em.resize((sw, sh))
            img.paste(new_em, (18, 400), new_em)

        with Image.open("C:\\Users\\1\\PycharmProjects\\emoji\\result2\\" + filenames[3]) as em:
            wbg = Image.new(mode="RGB", size=(sw, sh), color=(255, 255, 255))
            img.paste(wbg, (400, 400))
            em = em.convert("RGBA")
            new_em = em.resize((sw, sh))
            img.paste(new_em, (400, 400), new_em)
        img.save("C:\\Users\\1\\PycharmProjects\\emoji\\result3\\" + str(num) + ".jpeg")
    filenames = filenames[4:]


