# python-YouTube-downloader
 Download videos from YouTube to mp3 or mp4 format
 
### Install python
 Download and install python version 3 for your OS [python](https://www.python.org/downloads/)  
 **Tip:** *Don't forget to Add Python to PATH (check box)*
 ![python_checkbox](https://user-images.githubusercontent.com/57621362/119864319-30e4e580-bf23-11eb-8c85-87fb428b5b32.jpg)
 
### Download ZIP
 1. Download zip and extract files
 2. Move Downloader.py inside the python folder, where the python exe is.  Example 'C:\Users\username\AppData\Local\Programs\Python\Python38'
 3. Create a folder wherever you want and move inside there the 'YouTube Downloader.bat'


### Download FFmpeg
 Download FFmpeg for your OS from [ffmpeg](https://ffmpeg.org/download.html)  
 Extract the zip file (for Windows systems ffmpeg-4.4-full_build.7z)  
 Move the 3 exe files (ffmpeg, ffplay, ffprobe) inside the folder with the YouTube Downloader.bat
 
### Install requirements
 1. Open cmd and move where you extracted the 'requirements.txt'
 2. pip install -r requirements.txt


### Edit batch file
 This is the batch file template:
 ```
 "Path where your Python exe is path\python.exe" "Path where your Python script is path\script name.py"
 pause
 ```
 In our case both python.exe and Downloader.py are in the same folder.
 So, it should be something like this:
 ```
 "C:\Users\theodoros\AppData\Local\Programs\Python\Python38\python.exe" "C:\Users\theodoros\AppData\Local\Programs\Python\Python38\Downloader.py"
 pause
 ```
 
### Run the app
 Now you should be able to run the app 'YouTube Downloader.bat' without any problem!
 ![YouTube Downloader](https://user-images.githubusercontent.com/57621362/119863570-5fae8c00-bf22-11eb-91a1-c8ff11eba981.jpg)
 
## Enjoy!
