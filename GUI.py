import PySimpleGUI as sg
from b64_vars import *

sg.theme("DarkBlue16")
sg.theme_border_width(0)

layout = [[sg.Text("Reverse search an image!\nBegin by taking a snip or selecting an image.",
                   font=("Dubai", 20), justification="c")],

          [sg.Button("Take snip!", font=("Dubai", 14), key="-SNIP_BUTTON-", tooltip="When clicked, you will have to"
                                                                                    "\ntake a snip of the screen.")],

          [sg.InputText("", font=("Dubai", 14), key="-FILE_PATH-", justification="c"),
           sg.FileBrowse(font=("Dubai", 12), tooltip="Look for a file on your device")],

          [sg.Button("Reverse Search!", font=("Dubai", 14), pad=(0, 20), key="-SEARCH_BUTTON-",
                     tooltip="Search the image and get the link.")],

          [sg.InputText("", font=("Dubai", 14), readonly=True, justification="c", key="-LINK-",
                        disabled_readonly_background_color=sg.theme_input_background_color()),
           sg.Button("", image_data=copy_link, key="-COPY_LINK-", tooltip="Copy the link to the clipboard"
                     , button_color=(sg.theme_background_color(), sg.theme_background_color())),
           sg.Button("", image_data=open_link, key="-OPEN_LINK-", tooltip="Open the link in the browser",
                     button_color=(sg.theme_background_color(), sg.theme_background_color()))]]


win = sg.Window("Image Reverse Search", layout, element_justification="c", use_default_focus=False, resizable=True,
                icon=search)
