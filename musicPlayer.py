#from playsound import playsound
import pygame
from tkinter import *
from mutagen.mp3 import MP3
import time
import os

root = Tk()
root.geometry("400x400+900+100")
root.title("Music Player")
pygame.mixer.init()




directory = str(input("What's the directories name? "))
folder = os.fsencode(directory)


#duration = int(mp3File.info.length)
songI = 0

paused = False


songs = []
for file in os.listdir(folder):
	filename = os.fsdecode(file)
	#print(filename)
	if filename.endswith(".mp3") == True:
		songs.append(str(file))
		currentSong = file
		amountSongs = len(songs)
		for i in range(amountSongs):
			#pygame.mixer.music.queue(songs[i])
			print(songs[i])
		#print(songs)



songFile = currentSong
mp3File = MP3(songFile)
audioLength = int(mp3File.info.length)



pos = pygame.mixer.music.get_pos()
def start():
	pygame.mixer.music.load(currentSong)
	pygame.mixer.music.play()
	global audioLength
	while audioLength > 0 and paused != True:
		audioLength -= 1
		time.sleep(1)
		print(audioLength)
		root.update()
		#root.update_idletasks()

def pause():
	pygame.mixer.music.pause()
	paused = True
	#updateDurationLabel()

def play():
	pygame.mixer.music.unpause()
	paused = False

def restart():
	pygame.mixer.music.rewind()

startButton = Button(root, text="Start Song", command=start)
startButton.grid(row=1, column=3)

pauseButton = Button(root, text="Pause", command=pause)
pauseButton.grid(row=0, column=3)

playButton = Button(root, text="Play", command=play)
playButton.grid(row=2, column=3)

restartButton = Button(root, text="Restart Song", command=restart)
restartButton.grid(row=3, column=3)

audioLengthLabel = Label(root, textvariable=audioLength)
audioLengthLabel.grid(row=5, column=3)

#playsound('viceCity.mp3')
#root.update_idletasks()

mainloop()