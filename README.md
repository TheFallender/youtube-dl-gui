# Youtube-Dl-GUI by TheFallender
Simple Youtube-DL GUI made with PySimpleGUI.

## Installation
You can use the .exe on the release or open the .pyw with py after installing the requirements.

Requirements
1. In any case, you will need to have youtube-dl installed.
```
    pip install youtube-dl
```
2. Then you should install the requirements with pip.
```
    pip install requirements.txt
```
3. If you are on Linux you will need to also have installed tinker.
```
    sudo apt-get install python3-tk
```
Optional: If you want to use the merge of the video and the audio you will need to have ffmpeg. You can download it at [ffmpeg](https://ffmpeg.org/download.html)
Note: On Linux it seems that ffmpeg doesn't support the latest Youtube Codec so you won't be able to merge the files.

## Build
If you want to build it yourself, you'll have to use pyinstaller:
```
    pyinstaller --onefile --icon=app.ico Youtube-DL-GUI.pyw
```

## TODO
Save the latest settings if clicked on a button.
