from PIL import Image, ImageDraw, ImageFont


class Watermark(object):
    def process(self, img):
        font = ImageFont.load_default().font
        #font = ImageFont.truetype("fonts/arialbd.ttf",40)
        #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf',15)
        draw = ImageDraw.Draw(img)
        draw.text((50,50), "PYTHONX",font=font, fill=('#f0f0f0'))
        #draw.line((0, 0) + img.size, fill=128)
        #draw.line((0, img.size[1], img.size[0], 0), fill=128)
        return img


class Watermark_opacity(object):
    def process(self, img):
        base = img.convert('RGBA')
        width, height = base.size

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

        # get a font
        #fnt = ImageFont.load_default(50).font
        try:
            # For Linux
            fnt = ImageFont.truetype("DejaVuSans.ttf", 60)
        except Exception:
            print("No font DejaVuSans; use default instead")
            # For others
            fnt = ImageFont.load_default()
        # get a drawing context
        d = ImageDraw.Draw(txt)

        x = width / 2
        y = height / 2

        # draw text, half opacity
        d.text((x, y), "PythonX", font=fnt, fill=(255, 255, 255, 60))
        txt = txt.rotate(45)

        img = Image.alpha_composite(base, txt)
        return img