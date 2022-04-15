import time
import playsound
from sys import exit 
while True:
  print("Hello! Welcome to the timer!")
  secs = input("How many seconds?\n")
  secs = int(secs)
  secs += 1
  for i in reversed(range(secs)):
    print(i,"seconds left!", end="\r")
    time.sleep(1)
  print("Timer complete!")
  playsound.playsound('sound.mp3')
  again = input("Would you like to start another timer? (reply with y/n)")
  if again == "n" or again == "N":
    exit(0)

