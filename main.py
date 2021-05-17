import time
import playsound
print("Hello! Welcome to the timer!")
secs = input("How many seconds?\n")
secs = int(secs)
secs += 1
for i in reversed(range(secs)):
  print(i,"seconds left!")
  time.sleep(1)
print("Timer complete!")
# will not work on offline IDE
playsound.playsound('sound.mp3')