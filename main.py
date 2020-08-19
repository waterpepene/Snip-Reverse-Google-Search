from GUI import *
from functions import *
from os import path, getcwd
from pyperclip import copy
from webbrowser import open

while True:
    event, values = win.Read()

    if event == sg.WIN_CLOSED:
        quit("Window Closed")

    if event in "-SNIP_BUTTON-":
        takeSnip()
        win["-LINK-"].update(searchImage(path.abspath(getcwd() + "/image.png")))      # Gets path to the image

    if event in "-SEARCH_BUTTON-":
        win["-LINK-"].update(searchImage(values["-FILE_PATH-"]))                      # Searches for the image

    if event in "-COPY_LINK-":
        copy(values["-LINK-"])

    if event in "-OPEN_LINK-":
        open(values["-LINK-"])