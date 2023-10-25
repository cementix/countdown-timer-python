from playsound import playsound
# function that allows us to play the sound by simply calling playsound("the-name-of-the-sound.mp3")
import time

CLEAR = "\033[2J" # clears entire terminal (the program will then print the statement at the bottom of the alarm function)
CLEAR_AND_RETURN = "\033[H" # then this will clear the terminal and return the function again, printing over the previous function output

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) # makes the program wait for 1 second. without it the program will run as fast as the computer can run it 
        time_elapsed += 1 # adds 1 second after every loop

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # indeger division(e.g: 125 // 60 = 2 because 60 evenly divides 125 two times)
        seconds_left = time_left % 60 # the remainder after division (e.g: 125 % 6 = 5)

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
        # :02d = make this number a 2 digits number and add a leading 0 if it's not 2 digits already

    playsound("alarm-sound.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)



