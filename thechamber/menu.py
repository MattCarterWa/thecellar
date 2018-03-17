import easygui
import os
import report
from gmail import send_attached_file

storage_path = "menu_cellar"
menu_storage_ext = ".ms"
split_key = ":"



class Menu:
    no_choice_msg = "Please select an option"
    about_to_exit_msg = "Would you like to quit?"
    menu_msg = ""
    options = []
    title = ""
    selection = None

    @staticmethod
    def load_menu_options(title):
        options = []
        programs = []
        if not title:
            return []
        else:
            file_name = "".join((title, menu_storage_ext))
            file_path = os.path.join(storage_path, file_name)

            try:
                with open(file_path, "r") as f:
                    for l in f:
                        option = l.split(split_key)
                        options.append(option[0])
                        programs.append(option[1])
                return options, programs

            except:
                msg = "".join(("We couldn't find menu items for this menu: ", title))
                easygui.msgbox(msg)
                return None


class LabelMenu(Menu):
    title = "Label Menu"
    no_choice_msg = "Please select an option"
    menu_msg = "What Labels do you need?"
    menu_no_program_msg = "That program is not available yet!"
    label_menu_options, label_menu_programs, = Menu.load_menu_options(title)

    def __init__(self):
        self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.label_menu_options)

        while not self.user_selection:
            user_close = easygui.ynbox(self.about_to_exit_msg)

            if user_close == True:
                quit()

            else:
                easygui.msgbox(self.no_choice_msg)
                self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.label_menu_options)

        index_of_program = self.label_menu_options.index(self.user_selection)
        program = self.label_menu_programs[index_of_program]
        if program is None:
            easygui.msgbox(self.menu_no_program_msg)
            pass
        else:
            program = "".join(("self.", program))
            eval(program)

    def run_f4t_page(self):
        from salvage_label import create_salvage_page

        path = create_salvage_page()

        answer = easygui.ynbox("Want me to email this?")

        if not answer:
            quit()

        else:
            send_to = easygui.enterbox("Who am I sending this to?", "Enter Email")

            while not answer:
                msg = "".join(("Is this correct\n", send_to))
                easygui.ynbox(msg)
            msg_body = "Please print this out on an F4T Tag Sheet,\nThanks - Matt"
            send_attached_file(send_to,"F4T Salvage Tags", msg_body, path)





class MainMenu(Menu):
    title = "Main Menu"
    no_choice_msg = "Please select an option"
    menu_msg = "What do you need to do?"
    menu_no_program_msg = "That program is not available yet!"
    main_menu_options, main_menu_programs = Menu.load_menu_options(title)

    def __init__(self):
        self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.main_menu_options)
        # print(menu_select)

        while not self.user_selection:
            user_close = easygui.ynbox(self.about_to_exit_msg)

            if user_close == True:
                quit()

            else:
                easygui.msgbox(self.no_choice_msg)
                self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.main_menu_options)

        index_of_program = self.main_menu_options.index(self.user_selection)
        program = self.main_menu_programs[index_of_program]
        if program is None:
            easygui.msgbox(self.menu_no_program_msg)
            pass
        else:
            program = "".join(("self.", program))
            eval(program)
        # print(program)

    def run_scan(self):
        print("Reached")
        import scanner

    def run_report(self):
        ReportMenu()

    def run_label(self):
        LabelMenu()



class ReportMenu(Menu):
    title = "Report Menu"
    no_choice_msg = "Please select an option"
    menu_msg = "What Report do you need?"
    menu_no_program_msg = "That Report is not available yet!"
    report_menu_options, report_menu_programs = Menu.load_menu_options(title)

    def __init__(self):
        self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.report_menu_options)
        # print(menu_select)

        while not self.user_selection:
            user_close = easygui.ynbox(self.about_to_exit_msg)

            if user_close == True:
                quit()

            else:
                easygui.msgbox(self.no_choice_msg)
                self.user_selection = easygui.choicebox(self.menu_msg, self.title, self.report_menu_options)

        index_of_program = self.report_menu_options.index(self.user_selection)
        program = self.report_menu_programs[index_of_program]
        if program is None:
            easygui.msgbox(self.menu_no_program_msg)
            pass
        else:
            program = "".join(("self.", program))
            eval(program)
            # print(program)

    def run_quantity_report(self):
        report.QuantityReport()




