import datetime
import easygui
from datetime import date, time
import os
todays_date = str(date.today())
starttime = (str(datetime.datetime.now().time())).split(":")
current_time = ".".join((starttime[0], starttime[1]))
timestamp = "_".join((todays_date, current_time))
scan_ext = ".txt"
folder = "scan_files_cellar"


def run_scan(scan_type="Unnamed Scan"):
    pass


def save_scan(scan, filename):
    full_file_name = "".join((filename, scan_ext))
    print(full_file_name)
    file_path = os.path.join(os.getcwd(), folder, full_file_name)
    print(file_path)
    with open(file_path, "w") as f:
        f.write(scan)


run_scan()
#print(timestamp)

