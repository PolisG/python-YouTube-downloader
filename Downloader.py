from __future__ import unicode_literals
import os
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root= tk.Tk()
root.title('YouTube downloader')

def select_folder():
        # Select and return folder path
        global folder_path
        folder_path = StringVar()
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
        entry1.delete(0, tk.END)
        folder = folder_path.get()
        folder_path.set(os.path.abspath(os.getcwd()))
        label2.config(text='Save to: '+folder_path.get(), font=('Arial', 11))
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': folder + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
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
            'format': 'bestvideo+bestaudio',
            'videoformat': 'mp4',
            'outtmpl': folder + '/%(title)s.%(ext)s',
            #'subtitleslangs': 'en',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

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

button3 = tk.Button(root, text=' Download mp4 ', command=download_mp4, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(320, 260, window=button3)

button4 = tk.Button(root, text='Exit Application', command=root.destroy, bg='light slate gray', font=('Arial', 11, 'bold'))
canvas1.create_window(320, 320, window=button4)

root.mainloop()