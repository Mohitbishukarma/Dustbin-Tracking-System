# IMPORTING MODULES/LIBRARY
from  tkinter import *
import pathlib
import home
import dust_bin_list
import system_info
import status



# WINDOW CONFIG
window = Tk()
window.title("Waste Management System")
window.geometry("1000x600")
window.configure(bg="#FFFFFF")

# APP LOGIC

# PATH FOR THE ASSETS
BASE_PATH = pathlib.Path(str(pathlib.Path(__file__)).replace('main.py',''))
def absolute_path(file_name):
    ASSETS_PATH = BASE_PATH / pathlib.Path("assets") / file_name
    return ASSETS_PATH

# REQUIRD IMAGES LOASDING
home_button_clicked_image = PhotoImage(file=absolute_path("buttons/home_button_clicked.png"))
status_view_button_clicked_image = PhotoImage(file=absolute_path("buttons/status_view_button_clicked.png"))
dust_bin_list_button_clicked_image = PhotoImage(file=absolute_path("buttons/dust_bin_list_button_clicked.png"))
system_info_button_clicked_image = PhotoImage(file=absolute_path("buttons/system_info_button_clicked.png"))
status_box_image = PhotoImage(file=absolute_path("img/status_box.png"))
logo = PhotoImage(file=absolute_path("img/logo.png"))
# system_cycle = PhotoImage(file=absolute_path("img/system_cycle.png"))
# system_cycle = Image()
# system_cycle = ImageTk(i)

window.iconphoto(False, logo)
def delete_content_inside_content_view():
    for widget in content_view.winfo_children():
        widget.destroy()

def change_to_default_state():
    home_button.configure(image = home_button_image)
    status_view_button.configure(image = status_view_button_image)
    dust_bin_list_button.configure(image = dust_bin_list_button_image)
    system_info_button.configure(image = system_info_buttton_image)


def home_view():
    delete_content_inside_content_view()
    home.make_home_view(content_view, {"logo":logo,})

def status_view_view() -> None:
    delete_content_inside_content_view()
    status.make_status_view(content_view, {'status_box_image': status_box_image,}, content_view)


def dust_bin_list_view():
    delete_content_inside_content_view()
    dust_bin_list.make_dust_bin_list_view(content_view)

def system_info_view():
    delete_content_inside_content_view()
    system_info.make_system_info_view(content_view)

def handle_home_button(event):
    home_view()
    change_to_default_state()
    event.widget.configure(image = home_button_clicked_image)


def handle_status_view_button(event):
    status_view_view()
    change_to_default_state()
    event.widget.configure(image = status_view_button_clicked_image)


def handle_dust_bin_list_button(event):
    dust_bin_list_view()
    change_to_default_state()
    event.widget.configure(image = dust_bin_list_button_clicked_image)


def handle_system_info_button(event):
    system_info_view()
    change_to_default_state()
    event.widget.configure(image = system_info_button_clicked_image)


# SIDEBAR
sidebar = Frame(window)
sidebar.pack(side=LEFT)
sidebar.pack_propagate(False)
sidebar.configure(width=277, height=600, bg="#EEF7FC")
canvas = Canvas(
    sidebar,
    bg = "#EEF7FC",
    height = 600,
    width = 277,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.pack()
canvas.create_text(
    18.0,
    15.999999999999986,
    anchor="nw",
    text="Waste Management",
    fill="#2F3061",
    font=("Lato SemiBold", 24 * -1)
)

canvas.create_text(
    18.0,
    57.999999999999986,
    anchor="nw",
    text="System",
    fill="#2F3061",
    font=("Lato SemiBold", 24 * -1)
)

# HOME BUTTON
home_button_image = PhotoImage(file=absolute_path("buttons/home_button.png"))
home_button = Button(
    image=home_button_image,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
home_button.place(
    x=19.0,
    y=147.0,
    width=238.0-3,
    height=31.0+3
)
home_button.bind("<Button-1>",handle_home_button)


# STATUS VIEW BUTTON
status_view_button_image = PhotoImage(
    file=absolute_path("buttons/status_view_button.png"))
status_view_button = Button(
    image=status_view_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("status_view_button clicked"),
    relief="flat"
)
status_view_button.place(
    x=19.0,
    y=178.0+5,
    width=238.0-3,
    height=31.0+3
)
status_view_button.bind("<Button-1>",handle_status_view_button)


# DUST BIN LIST BUTTON
dust_bin_list_button_image = PhotoImage(
    file=absolute_path("buttons/dust_bin_list_button.png"))
dust_bin_list_button = Button(
    image=dust_bin_list_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("dust_bin_list_button clicked"),
    relief="flat"
)
dust_bin_list_button.place(
    x=19.0,
    y=209.0+10,
    width=238.0-3,
    height=31.0+3
)
dust_bin_list_button.bind("<Button-1>", handle_dust_bin_list_button)


# SYSTEM INFO BUTTON
system_info_buttton_image = PhotoImage(
    file=absolute_path("buttons/system_info_button.png"))
system_info_button = Button(
    image=system_info_buttton_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("system_info_button clicked"),
    relief="flat"
)
system_info_button.place(
    x=19.0,
    y=240.0+15,
    width=238.0-3,
    height=31.0+3
)
system_info_button.bind("<Button-1>", handle_system_info_button)


# CONTENT FRAME
content_view = Frame(window)
content_view.pack(side=LEFT)
content_view.pack_propagate(False)
content_view.configure(bg="#FFFFFF", width=(1000-277), height= 600)


#INITIAL PAGE
def first_run():
    home_button.config(image=home_button_clicked_image)
    home_view() 

first_run()

window.resizable(False,False)
window.mainloop() # APP LOOP
