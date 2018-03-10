from PIL import ImageFont


class Font():
    location = None
    render = None
    text = "None"

class SalvageHeaderText():
    location = (10, 90)
    size = 15
    fill = "Black"
    render = ImageFont.truetype("arial.ttf", size=size)
