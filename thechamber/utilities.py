from datetime import datetime, date

todays_date = str(date.today())
starttime = (str(datetime.now().time())).split(":")
current_time = ".".join((starttime[0], starttime[1]))
timestamp = "_".join((todays_date, current_time))
font_folder = "font_cellar"
label_folder = "label_files_cellar"
todays_salvage_page_path = "label_files_cellar/todayspage.png"

# Email Related
program_email = "fmphotocenter@gmail.com"

def na_date():
    segments = todays_date.split("-")
    na_date = "/".join((segments[1], segments[2], segments[0]))
    return na_date

# from salvage_label import create_salvage_page

def center_image(container_size, object_size):
    x = int(1/2 * (container_size[0] - object_size[0]))
    y = int(1/2 * (container_size[1] - object_size[1]))
    return (x, y)

class matrix_printer():


    def __init__(self, starting_x, starting_y, terminate_a, terminate_b, object_size):
        self.a = 0
        self.b = 0
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.terminate_a = terminate_a
        self.terminate_b = terminate_b
        self.current_x = starting_x
        self.current_y = starting_y
        self.complete = False
        self.width = object_size[0]
        self.height = object_size[1]

    @property
    def x(self):
        if self.a == self.terminate_a:
            self.a = 0
            self.b += 1
            if self.b == self.terminate_b:
                self.complete = True



        self.current_x = self.a * self.width + self.starting_x + self.a * 45

        return self.current_x

    @property
    def y(self):
        if self.b == self.terminate_b:
            self.complete = True
            return 3308
        self.current_y = self.b * self.height + self.starting_y + self.b * 70
        self. a +=1
        return self.current_y

    @property
    def coords(self):
        her = self.x
        him = self.y
        return (her, him)

# print(na_date())

#printer = matrix_printer(0, 0)
