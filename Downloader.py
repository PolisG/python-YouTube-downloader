from __future__ import unicode_literals
import os
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root= tk.Tk()
root.title('YouTube downloader')

folder_path = StringVar()
kbps_select = StringVar()

option_kbps = [
    '192',
    '256',
    '320',
]

kbps_select.set(option_kbps[2])

def select_folder():
        # Select and return folder path
        folder_selected = filedialog.askdirectory(parent=root, initialdir="/")
        if folder_selected:
            folder_path.set(folder_selected)
            folder_path.get()
        else:
            folder_path.set(os.path.abspath(os.getcwd()))
            folder_path.get()
        label2.config(text='Save to: '+folder_path.get(), font=('Arial', 11))

def download_mp3():
        link = entry1.get()
        folder = folder_path.get()
        kbps = kbps_select.get()
        
        entry1.delete(0, tk.END)
        folder_path.set(os.path.abspath(os.getcwd()))
        label2.config(text='Save to: '+folder_path.get(), font=('Arial', 11))
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': folder + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': kbps,
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

def download_mp4():
        link = entry1.get()
        entry1.delete(0, tk.END)
        folder = folder_path.get()
        folder_path.set(os.path.abspath(os.getcwd()))
        label2.config(text='Save to: '+folder_path.get(), font=('Arial', 11))

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
            'videoformat': 'mp4',
            'outtmpl': folder + '/%(title)s.%(ext)s',
            'writesubtitles': True,
            'subtitle': '--write-sub --sub-lang en',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
'''
def download_auto_subs():
        link = entry1.get()
        entry1.delete(0, tk.END)
        folder = folder_path.get()
        folder_path.set(os.path.abspath(os.getcwd()))
        label2.config(text='Save to: '+folder_path.get(), font=('Arial', 11))

        ydl_opts = {
            #'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
            #'videoformat': 'mp4',
            'outtmpl': folder + '/%(title)s.%(ext)s',
            'writesubtitles': True,
            'subtitle': '--write-auto-sub --convert-subs=srt --skip-download --sub-lang=en',
            #'postprocessors': [{
                #'key': 'FFmpegVideoConvertor',
                #'preferedformat': 'mp4',
            #}],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
'''

# Create GUI screen.
canvas1 = tk.Canvas(root, width = 640, height = 360)
canvas1.pack()

# Labels can be used to print text on top of the Canvas.
label1 = tk.Label(root, text='Insert YouTube link to download')
label1.config(font=('Arial', 18))
canvas1.create_window(320, 40, window=label1)

# Entry boxes are used to collect information from the user.
entry1 = tk.Entry(root, width=48) # YouTube link has 43 chars (id is always 11 characters)
canvas1.create_window(320, 80, window=entry1)

button1 = tk.Button(root, text=' Select folder ', command=select_folder, bg='azure3', font=('Arial', 11, 'bold'))
button1.pack()
canvas1.create_window(320, 120, window=button1)

label2 = tk.Label(root)
label2.pack()

label3 = tk.Label(root, text='Select format')
label3.config(font=('Arial', 18))
canvas1.create_window(320, 180, window=label3)

button2 = tk.Button(root, text=' Download mp3 ',command=download_mp3, bg='palegreen2', font=('Arial', 11, 'bold'))
canvas1.create_window(320, 220, window=button2)

# Create Dropdown Menu
drop1 = tk.OptionMenu(root, kbps_select, *option_kbps)
drop1.pack()
canvas1.create_window(440, 220, window=drop1)

button3 = tk.Button(root, text=' Download mp4 ', command=download_mp4, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(320, 260, window=button3)

#button4 = tk.Button(root, text=' Download auto subs ', command=download_auto_subs, bg='lightskyblue2', font=('Arial', 11, 'bold'))
#canvas1.create_window(490, 260, window=button4)

button5 = tk.Button(root, text='Exit Application', command=root.destroy, bg='light slate gray', font=('Arial', 11, 'bold'))
canvas1.create_window(320, 320, window=button5)

root.mainloop()