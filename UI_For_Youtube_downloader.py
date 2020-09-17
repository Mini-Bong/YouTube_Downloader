import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
def browser_button():
    filename = filedialog.askdirectory()
    return filename
def DownLoadVideo():
    link = urlEntry.get()
    yt = YouTube(link)
    Label(box, text='Downloading.......').place(x = 100, y = 255)
    filters = yt.streams.filter(progressive= True, file_extension = 'mp4')
    filters.get_highest_resolution().download(output_path=browser_button())
    Label(box, text='Download Competed').place(x = 100, y = 255)

box  = tk.Tk()
box.geometry("600x600")
box.title("Youtube Donwloader")
C = Canvas(box, bg='blue', height= 250, width = 300)
searchBox = tk.Label(box, text = "YouTube URL")
searchBox.place(x = 250, y =100)
urlEntry = tk.Entry(box, width = 40)
urlEntry.place(x =100, y = 200, width = 400)
downloadButton = tk.Button(box, text = "Download", bg = 'blue', command = DownLoadVideo) 
downloadButton.place(x =250, y=300, width = 75)
box.mainloop()