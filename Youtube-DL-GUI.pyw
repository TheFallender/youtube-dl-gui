import os
import subprocess
from io import BytesIO
import webbrowser
import requests
import PySimpleGUI as sg
import PIL.Image as Image
import PIL.ImageTk as ImageTk

# Get the default download path
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

# First is only needed when Tinker has not been initialized
def get_img_data(url, maxsize=(320, 180), first= False):
    # Get the image from the url
    response = requests.get(url, stream=True)

    # Transform the bytes into an Image
    responseImage = Image.open(BytesIO(response.content))

    # Adjust image size
    responseImage.thumbnail(maxsize)

    if first:
        # Create a temp BytesIO
        imageBytesIO = BytesIO()

        # Save in imageBytesIo
        responseImage.save(imageBytesIO, format="PNG")

        # Delete the img
        del responseImage

        # Return the bytes from the image
        return imageBytesIO.getvalue()

    # Return the image
    return ImageTk.PhotoImage(responseImage)

# Theme
sg.theme("DarkAmber")

# Variables
imgOnline = sg.Text("Image not found, is there an active internet connection?", pad=(0, 30))
iconToShow = None
try:
    imgOnline = sg.Image(data=get_img_data("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/YouTube_icon.png/800px-YouTube_icon.png", first = True), size = (320, 180), enable_events=True, key="-IMAGE_CLICK-", pad=(0, 30))
    iconToShow = get_img_data("https://raw.githubusercontent.com/TheFallender/youtube-dl-gui/master/app.ico", maxsize=(256,256), first=True)
except:
    pass
vidUrl = ""
runWindow = True

# Layout
appLayout = [
    [
        sg.Text("  Youtube DL GUI by TheFallender  ", text_color="BLACK", background_color="WHITE", relief=sg.RELIEF_RAISED, border_width=5),
    ],
    [
        sg.Text("G̲i̲t̲H̲u̲b̲ R̲e̲po̲", background_color="WHITE", text_color="BLUE", relief=sg.RELIEF_GROOVE, border_width=4, enable_events=True, key="-GITHUB_CLICK-")
    ],
    [
        imgOnline
    ],
    [
        sg.Text("Youtube Link: "),
        sg.InputText(size=(25,1), key = "-URL_INPUT-"),
    ],
    [
        sg.Checkbox("Show Advanced", default = False, key="-CB_ADV-", enable_events=True),
        sg.Checkbox("Show CMD", default = True, key="-CB_CMD-")
    ],
    [
        sg.Text("Format: ", key = "-INFO_F-", visible=False),
        sg.InputText(default_text="bestvideo+bestaudio", size=(25,1), key = "-PARAM_F-", visible=False),
    ],
    [
        sg.Text("Download Location: ", key = "-INFO_O-", visible=False),
        sg.InputText(default_text=get_download_path(), size=(25,1), key = "-PARAM_O-", visible=False),
    ],
    [
        sg.Text("Filename format: ", key = "-INFO_FN-", visible=False),
        sg.InputText(default_text="%(title)s.%(ext)s", size=(25,1), key = "-PARAM_FN-", visible=False),
    ],
    [
        sg.Text("Extra Parameters: ", key = "-INFO_E-", visible=False),
        sg.InputText(default_text="--merge-output-format mp4", size=(25,1), key = "-PARAM_E-", visible=False),
    ],
    [
        sg.Text("Cmd: ", key="-COMMAND-", visible=False, pad=(0,(20,10)))
    ],
    [
        sg.Button('Download', pad=(5,(20,10))),
        sg.Button('Cancel', pad=(5,(20,10))),
    ]
]

# Create the window
window = sg.Window("Youtube DL GUI", appLayout, element_justification='c', icon=iconToShow)

# Event Loop
while runWindow:
    event, values = window.read()

    if event == "-GITHUB_CLICK-":
        webbrowser.open('https://github.com/TheFallender/youtube-dl-gui')

    if event == "-IMAGE_CLICK-":
        webbrowser.open('https://www.youtube.com')

    if event == "-CB_ADV-":
        val = values["-CB_ADV-"]
        window['-INFO_F-'].Update(visible=val)
        window['-PARAM_F-'].Update(visible=val)
        window['-INFO_O-'].Update(visible=val)
        window['-PARAM_O-'].Update(visible=val)
        window['-INFO_FN-'].Update(visible=val)
        window['-PARAM_FN-'].Update(visible=val)
        window['-INFO_E-'].Update(visible=val)
        window['-PARAM_E-'].Update(visible=val)
        window['-CB_ADV-'].Update(disabled=True)

    if event == "Download" and values['-URL_INPUT-'] != "":
        # Format the command with the given input
        command = "youtube-dl -f {0} -o \"{1}\\{2}\" {3} ".format(values['-PARAM_F-'], values['-PARAM_O-'], values['-PARAM_FN-'], values['-PARAM_E-'])
        command += values['-URL_INPUT-']
        
        # Wether or not to show a Command Prompt
        if values['-CB_CMD-']:
            cmdShow = 'cmd /c (echo Youtube-DL GUI by TheFallender: & echo Comand to run: & echo {0} & timeout 5 & echo. & {0})'.format(command)
            subprocess.call(cmdShow)
        else:
            subprocess.Popen(command, shell=True).communicate()
        
        runWindow = False

    if event == "Cancel" or event == sg.WIN_CLOSED:
        runWindow = False

window.close()