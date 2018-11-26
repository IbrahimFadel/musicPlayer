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
	global audioLength
	audioLengthText = str(audioLength)
	pygame.mixer.music.load(currentSong)
	pygame.mixer.music.play()
	while audioLength > 0 and paused != True:
		audioLength -= 1
		time.sleep(1)
		#print(audioLength)
		audioLengthText = str(audioLength)
		print(audioLengthText)
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
	pygame.mixer.music.play()

startButton = Button(root, text="Start Song", command=start)
startButton.grid(row=0, column=6)

pauseButton = Button(root, text="Pause", command=pause)
pauseButton.grid(row=1, column=6)

playButton = Button(root, text="Play", command=play)
playButton.grid(row=1, column=4)

restartButton = Button(root, text="Restart Song", command=restart)
restartButton.grid(row=3, column=0)

audioLengthText = StringVar()
audioLengthLabel = Label(root, text=audioLengthText)
audioLengthLabel.grid(row=5, column=3)

mainloop()