from tkinter import filedialog
from tkinter import * 
import pygame 
import os


root = Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init() #initiate mixer in python in order to play autio

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song, songs
    root.directory = filedialog.askdirectory()
    songs = [song for song in os.listdir(root.directory) if song.endswith('.mp3')]
    for song in songs: 
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = song[songlist.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused 
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused 

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label= 'Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15 )
songlist.pack() #add on window 

play_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\play.png")
pause_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\pause.png")
next_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\next.png")
prev_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\previous.png")

control_frame = Frame(root)
control_frame.pack() #"displays" frame


play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=prev_music)


play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()






