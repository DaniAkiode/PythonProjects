from tkinter import * 
import pygame 
import os


root = Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init() #initiate mixer in python in order to play autio


songlist = Listbox(root, bg="black", fg="white", width=100, height=15 )
songlist.pack() #add on window 

play_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\play.png")
pause_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\pause.png")
next_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\next.png")
prev_btn_image = PhotoImage(file="C:\\Users\\danny\\PythonProjects\\MusicPlayer\\previous.png")

control_frame = Frame(root)
control_frame.pack() #"displays" frame


play_btn = Button(control_frame, image=play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0)


play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()






