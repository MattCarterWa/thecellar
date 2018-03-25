import easygui
import os
from font import SalvageHeaderText
from PIL import Image, ImageDraw, ImageFont
from label import Label, label_storage, label_cellar
from utilities import na_date, label_folder, center_image, matrix_printer
from salvage_barcode import generate_barcode

todays_date = na_date()
default_division = "701"
default_store = "00688"

class SalvageLabel(Label):
    salvage_label_bg_filename = "salvage_label_bg.png"
    salvage_label_bg_path = os.path.join(os.getcwd(), label_folder, salvage_label_bg_filename)

    label_details = {"Name": "Salvage",
                     "Width": 275,
                     "Height": 120,
                     "Background Color": "White",
                     "Background Image": salvage_label_bg_path,
                     "Date XY": (151, 318),
                     "Barcode Text XY": (160, 157),
                     "Barcode Image XY": (87, 55)
                     }

    barcode_text = "".join(("701", "00688", todays_date.replace("/", "")))

    def __init__(self, division=default_division, store=default_division):
        # print(self.label_details)
        self.barcode_text = "".join((division, store, todays_date.replace("/", "")))
        self.load_label()
        if "Background Image":
            self.im = Image.open(self.label_details["Background Image"])
            self.draw = ImageDraw.Draw(self.im)
            self.draw_text()
        else:
            self.im = Image.new("RGB", self.size, self.background_color)
            self.draw = ImageDraw.Draw(self.im)
            self.draw_text()

        # self.im.show()
        """What happens when I give a specific type of text to the label maker, or something in the future."""
        # print(self.label_details)


    def draw_text(self):
        if "Background Image":
            self.draw_date()
            self.draw_barcode_text()
            self.draw_barcode_image()
        else:
            pass

    def draw_fields(self):
        pass

    def draw_date(self):
        render_font = ImageFont.truetype("font_cellar/Consola.ttf", 21)
        self.draw.text(self.label_details["Date XY"], str(todays_date), font=render_font, fill="black")

    def draw_barcode_text(self):
        render_font = ImageFont.truetype("font_cellar/Consola.ttf", 31)
        self.draw.text(self.label_details["Barcode Text XY"], self.barcode_text, font=render_font, fill="black")
        pass

    def draw_barcode_image(self):
        im = generate_barcode(self.barcode_text)
        n_size = center_image(self.im.size, im.size)
        self.im.paste(im, (n_size[0], 55))
        pass

class SalvagePage:
    width = 2539
    height = 3307
    background = "label_files_cellar/salvage_page.png"
    terminate_a = 6
    terminate_b = 4
    starting_xy = (80,354)

    def __init__(self, label_im):
        self.salvage_page = Image.open(self.background)
        #bg_im.show()
        # print(label_im.size)
        printer = matrix_printer(self.starting_xy[0], self.starting_xy[1], self.terminate_a, self.terminate_b,
                                 (label_im.size[1], label_im.size[0]))
        #print(printer.x, printer.y)
        # bg_im.paste(label_im.rotate(90, expand=True), self.starting_xy)

        while not printer.complete:
            if printer.complete == True:
                break
            self.salvage_page.paste(label_im.rotate(90, expand=True), printer.coords)

        # self.salvage_page.show()

def create_salvage_page(division=default_division, store=default_store):
    page_creation_log = "_".join(("label_files_cellar/date_page_created", division, store)) + ".txt"
    path = "_".join(("label_files_cellar/todayspage", division, store)) + ".png"

    if not os._exists(page_creation_log):
        print("We didn't have this division_store combo.")
        with open(page_creation_log, "w") as f:
            f.write(todays_date)

    with open(page_creation_log, "r") as f:
        last_created_date = f.read()
        # print(last_created_date)

    if last_created_date != todays_date:
        print("Creating Salvage Page")
        with open(page_creation_log, "w") as f:
            f.write(todays_date)
        label = SalvageLabel(division, store)
        label.im.show()
        page = SalvagePage(label.im)
        page.salvage_page.save(path)
    return path

def check_create_salvage_page(division=default_division, store=default_store):
    path = create_salvage_page(division, store)
    return path


if __name__ == "__main__":
    # here = SalvageLabel()
    # for i in here.label_details:
        # print(i)
    #test_div="708"
    #test_store="00687"
    create_salvage_page()
    #print(todays_date)
