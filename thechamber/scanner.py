import easygui
import os
from utilities import todays_date, starttime, current_time, timestamp



folder = "scan_files_cellar"
scan_ext = ".txt"

class Scanner:
    scan_msg = "\n\n".join(("Scan UPCs into the blank field below. Click OK when done.",
                   "SKUs are not accepted yet."))

    scanner_title = "Basic Scanner"
    scanner_quit_msg = "Are you sure you want to exit the Scanner?"

    chose_scan_type_title = "Select Scan Type"
    chose_scan_type_msg = "Please select the type of your scan."

    @staticmethod
    def load_scan_types():
        file = "Scan Types"
        file_path = os.path.join(os.getcwd(), folder, file)
        with open(file_path, "r") as f:
            types = f.read()
            # print(types)
        return  types.split("\n")

    def save_scan(self):
        full_file_name = "".join((self.filename, scan_ext))
        # print(full_file_name)
        self.file_path = os.path.join(os.getcwd(), folder, full_file_name)
        # print(self.file_path)
        with open(self.file_path, "w") as f:
            f.write(self.scan)

    def start_scanning(self):
        self.scan = easygui.codebox(self.scan_msg, self.scanner_title)

    def set_filename(self, value):
        self.filename = "_".join((value, timestamp))

    def __init__(self):
        scan_types = Scanner.load_scan_types()
        self.scan = ""
        self.file_path = ""
        self.this_scan_type = easygui.choicebox(self.chose_scan_type_msg, self.chose_scan_type_title, scan_types)

        if not self.this_scan_type:
            self.set_filename("Scan")
            easygui.msgbox(" ".join(("This scan will use default name:", self.filename)))

        else:
            self.set_filename(self.this_scan_type)

        self.start_scanning()


        if not self.scan:
            while not self.scan:
                user_quit = easygui.ynbox(self.scanner_quit_msg)
                # print(user_quit)
                if user_quit:
                    quit()

                else:
                    self.start_scanning()

        self.save_scan()

Scanner()
