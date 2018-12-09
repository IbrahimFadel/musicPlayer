import time

songPlaying = False

def pause():
	global songPlaying
	songPlaying = False

def play():
	global songPlaying
	songPlaying = True

while songPlaying == True:
	print("It worked")

time.sleep(4)

play()