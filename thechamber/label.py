import easygui
import os
from font import SalvageHeaderText
from PIL import Image, ImageDraw

label_cellar = "label_files_cellar"
label_storage = ".lbl"

class Label():
    label_details = {"Name": "Salvage",
                     "Width": 100,
                     "Height": 50,
                     "Background Color": "White",
                     "Background Image": None
                     }

    @property
    def name(self):
        return self.label_details["Name"]

    @property
    def width(self):
        return int(self.label_details["Width"])

    @property
    def height(self):
        return int(self.label_details["Height"])

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def background_color(self):
        return self.label_details["Background Color"]

    def load_label(self):
        if "Background Image":
            return
        else:
            file = "".join((self.name, label_storage))
            path = os.path.join(os.getcwd(), label_cellar, file)
            with open(path, "r") as f:
                for line in f.readlines():
                    try:
                        field = line.split(":")

                        for i in range(len(field)):
                            field[i] = field[i].strip()

                        self.label_details[field[0]] = field[1]

                        # print(field)

                    except:
                        print("error")