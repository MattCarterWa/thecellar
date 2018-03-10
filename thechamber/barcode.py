from datetime import datetime
from utilities import center_image, font_folder
from isp_settings import division, store, salvage_text_font, salvage_font_size, salvage_padding, salvage_number_font, salvage_number_font_size
from PIL import ImageFont, Image, ImageDraw
from papers import Form

barcode_folder = "barcode_files_cellar"

def barcode_text():
    date = datetime.today()
    test = "%v%s%m%d%y".format(division, store, date.month, date.day, date.year)
    text = "".join((division, store, str(date.month), str(date.day), str(date.year)))
    return text

def get_barcode_image(user_typeface, barcode_text, label_size=(700, 200), font_size=(salvage_font_size)):
    formatted_text = "".join(("*", barcode_text, "*"))
    barcode_font = ImageFont.truetype("".join(("/", font_folder, "/", user_typeface)), font_size)
    barcode_image = Image.new("RGB", (label_size[0], label_size[1]), color="white")
    draw = ImageDraw.Draw(barcode_image)
    barcode_size = barcode_font.getsize(formatted_text)
    draw.text(center_image(label_size, barcode_size), formatted_text, font=barcode_font, fill="black")

    font = ImageFont.truetype("../fonts/"+salvage_number_font, salvage_number_font_size)
    size = font.getsize(barcode_text)
    # barcode_size = barcode_font.get_size(formatted_text)
    draw.text(center_image_below(label_size, size, barcode_size), barcode_text, font=font, fill="black")
    return barcode_image

def center_image_below(container, object, top_object):
    location = center_image(container, object)
    location = location[0], location[1] + top_object[1] + salvage_padding
    return location


def make_salvage_page(form_name="10032827"):
    form = Form(form_name)
    image = Image.new("RGB", form.paper_size, color="white")
    draw = ImageDraw.Draw(image)

    x, y = 0, 0
    label = get_barcode_image(salvage_text_font, barcode_text(), label_size=form.label_size)

    column, row = 1, 1
    origin_x = form.form_padding_left
    x = origin_x
    y = y + form.form_padding_top
    r = 0
    c = 0
    a, b = center_image(form.label_size, label.size)

    while c < form.max_column:

        while r < form.max_row:
            image.paste(label, (x, y))
            x = x + form.label_size[0] + form.label_padding_right
            r += 1
        y = y + form.label_size[1] + form.label_padding_bottom
        c += 1
        r = 0
        x = origin_x
    image.show()
    return image




# text = barcode_text()
# image = get_barcode_image(salvage_text_font, text)
# image.show()
barcode_page = make_salvage_page()
barcode_page.save("todayspage.png")