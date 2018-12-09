from tkinter import *
import time
import os
import pygame
from mutagen.mp3 import MP3
import random


root = Tk()
root.geometry("400x400+900+100")
root.title("Music Player")

pygame.mixer.init()
index = 0
var = IntVar()
def startSongs():
	pygame.mixer.music.load(playlistName + songs[index])
	pygame.mixer.music.play()
	#print(songPlaying)

def pause():
	pygame.mixer.music.pause()

def play():
	pygame.mixer.music.unpause()

def skip():
	global index
	song = MP3(playlistName + songs[index])
	audioLength = int(song.info.length)
	print(audioLength)
	pygame.mixer.music.set_pos(audioLength)
	if index == len(songs) - 1:
		index = 0
	else:
		index += 1
	startSongs()

def optionSelected():
	option = var.get()
	#print(option)

def shuffle():
	length = len(songs)
	order = []
	for i in range(length):
		rand = random.randint(0, length - 1)
		if(order.count(rand) > 0):
			return
		order.append(rand)
		#pygame.mixer.music.queue(songs[order[i]])
	print(order)


def repeatSong():
	print("hiya")

def onSelect(event):
	global var
	global index
	w = event.widget
	index = int(w.curselection()[0])
	#print(index)
	playButton = Button(root, text='Start Songs', command=startSongs)
	playButton.place(x=275, y=100)

	pauseButton = Button(root, text='Pause', command=pause)
	pauseButton.place(x=275, y=130)

	playButton = Button(root, text='Play', command=play)
	playButton.place(x=275, y=160)

	skipButton = Button(root, text='Skip', command=skip)
	skipButton.place(x=275, y=190)

	shuffleOption = Radiobutton(root, text="Shuffle", variable=var, value=1, command=shuffle).place(x=35, y=250)
	repeatOption = Radiobutton(root, text="Repeat Song", variable=var, value=2, command=optionSelected).place(x=35, y=270)
	
	return(index)


playlistName = input('Enter in the directory name: ')
directory = os.fsencode(playlistName)

songs = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp3") or filename.endswith(".wav"): 
        songs.append(filename)
        print(filename)
        continue
    else:
        continue

titleLabel = Label(root, text='Better Itunes :)')
titleLabel.place(x=150, y=30)

songListbox = Listbox(root, height=7)
songListbox.place(x=35, y=100)
songListbox.bind('<<ListboxSelect>>', onSelect)

for i in range(len(songs)):
	songListbox.insert(END, songs[i])	


mainloop()