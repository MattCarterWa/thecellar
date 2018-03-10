import json as jsonloader
from isp_settings import form_extension, form_property_char, form_directory, form_num_fields, accepted_papers, dpi
import os.path

def load_form(form_name):
    form_json = {}
    form_name = os.path.join(form_directory, form_name)

    if not form_extension in form_name:
        form_name = "".join((form_name, form_extension))

    with open(form_name, "r") as form:
        for line in form:
            #line = line.strip()
            element = line.split(form_property_char)
            if any(field in form_num_fields for field in element[0].split()):
                if "[" in element[1]:
                    element[1] = element[1].strip()[1:-1]
                    element[1] = element[1].split(",")
                    element[1] = float(element[1][0]), float(element[1][1])
                else:
                    element[1] = float(element[1])
            else:
                element[1] = element[1].strip()

            form_json[element[0]] = element[1]

    return form_json


class Form:
    def __init__(self, form_name):
        self.json = load_form(form_name)

    @property
    def form_name(self):
        return self.json["name"]

    @property
    def form_padding_left(self):
        return int(self.json["padding left"] * dpi)
    @property

    def form_padding_top(self):
        return int(self.json["padding top"] * dpi)

    @property
    def label_size(self):
        return (int(self.json["label size"][0] * dpi), int(self.json["label size"][1] * dpi))

    @property
    def label_padding_bottom(self):
        return int(self.json["label padding bottom"] * dpi)

    @property
    def label_padding_right(self):
        return int(self.json["label padding right"] * dpi)

    @property
    def max_num_of_tags(self):
        return self.max_column * self.max_row

    @property
    def max_column(self):
        return self.json["max column"]

    @property
    def max_row(self):
        return self.json["max row"]

    @property
    def paper_size(self):
        return (int(self.json["paper size"][0] * dpi), int(self.json["paper size"][1] * dpi))