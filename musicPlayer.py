from tkinter import *
import time
import os
import pygame


root = Tk()
root.geometry("400x400+900+100")
root.title("Music Player")

pygame.mixer.init()
index = 0


def startSongs():
	print(index)
	pygame.mixer.music.load('music/' + songs[index])
	pygame.mixer.music.play()

def pause():
	pygame.mixer.music.pause()

def play():
	pygame.mixer.music.unpause()

def skip():
	audioLength = int(songs[index].info.length)
	print(audioLength)

def onSelect(event):
	global index
	w = event.widget
	index = int(w.curselection()[0])
	print(index)
	playButton = Button(root, text='Start Songs', command=startSongs)
	playButton.place(x=275, y=100)

	pauseButton = Button(root, text='Pause', command=pause)
	pauseButton.place(x=275, y=130)

	playButton = Button(root, text='Play', command=play)
	playButton.place(x=275, y=160)

	skipButton = Button(root, text='Skip', command=skip)
	skipButton.place(x=275, y=190)
	return(index)



directory = os.fsencode('music')

songs = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp3"): 
        songs.append(filename)
        print(filename)
        continue
    else:
        continue

titleLabel = Label(root, text='Bootleg Itunes :)')
titleLabel.place(x=150, y=30)

songListbox = Listbox(root, height=7)
songListbox.place(x=35, y=100)
songListbox.bind('<<ListboxSelect>>', onSelect)

for i in range(len(songs)):
	songListbox.insert(END, songs[i])	



mainloop()