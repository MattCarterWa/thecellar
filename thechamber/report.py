import easygui
import os
from utilities import todays_date

scan_cellar = "scan_files_cellar"
no_scan_load_msg = "Are you sure you want to quit?"
report_cellar = "report_files_cellar"

class Report:
    name = ""
    ext = ".txt"

    @staticmethod
    def load_scan():
        scan_path = os.path.join(os.getcwd(), scan_cellar, "*.txt")
        file = easygui.fileopenbox(default=scan_path)

        while not file:
            response = easygui.msgbox(msg=no_scan_load_msg)
            if response:
                quit()
            else:
                file = easygui.fileopenbox(default=scan_path)

        with open(file, "r") as f:
            opened_file = f.read()

        return opened_file

class QuantityReport(Report):
    name = "Quanity Report"

    def __init__(self):
        scan = self.load_scan()
        scan = scan.split()
        self.catalogue = {}
        for record in scan:
            try:
                self.catalogue[record] += 1
            except KeyError:
                self.catalogue[record] = 1

        self.paper = ""

        for record in self.catalogue:
            upc_qntity = record, self.catalogue[record]
            self.paper = "".join((self.paper, self.new_line(upc_qntity)))

        self.save_report()

        print(self.paper)

    def save_report(self):
        file = "_".join((self.name,todays_date))
        path = os.path.join(os.getcwd(), report_cellar, "".join((file, self.ext)))
        with open(path, "w") as f:
            f.write(self.paper)

    def new_line(self, upc_qntity):
        upc_length = 12
        num_spaces = 4

        upc, quantity = upc_qntity
        user_enter = "_"*12

        if len(upc_qntity[0]) != 12:
            if len(upc) > 12:
                upc = str(upc) + " "*(num_spaces - (len(upc) - upc_length))
            else:
                upc = str(upc) + " "*(num_spaces + (upc_length - len(upc)))

        if len(str(quantity)) > 1:
            quantity = str(quantity) + " " * (num_spaces - (len(quantity) - 1))
        else:
            quantity = str(quantity) + " " * num_spaces

        return "".join(("\n", upc, quantity, user_enter))