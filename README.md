# Youtube-Dl-GUI by TheFallender
Simple Youtube-DL GUI made with PySimpleGUI.

## Installation
You can use the .exe on the release or open the .pyw with py after installing the requirements.

You can install the requirements with:
```
    pip install requirements.txt
```
If you are on Linux you will need to also have installed tinker, you can install it with: 
```
    sudo apt-get install python3-tk
```

If you want to use the merge of the files you will need to have ffmpeg.

Note: On Linux it seems that ffmpeg doesn't support the latest Youtube Codec so you won't be able to merge the files.

## Build
If you want to build it yourself, you'll have to use pyinstaller:
```
    pyinstaller.exe --onefile --icon=app.ico Youtube-DL-GUI.pyw
```


## TODO
Save the latest settings if clicked on a button.
