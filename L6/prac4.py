#Wapp to play a song
import pygame.mixer
import time
import webbrowser
while True:
	time.sleep(10)
	print("Drink water")
	pygame.mixer.init()
	pygame.mixer.music.load("alarm.mp3")
	pygame.mixer.music.play(1)
	webbrowser.open("www.google.com")
	time.sleep(2)
	pygame.mixer.music.stop()
	