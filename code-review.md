# Code Review: timer.py

### Issues Identified:

1. **Line too long (E501)**:

   - The following lines exceed 79 characters:
     - Line 2: `# function that allows us to play the sound by simply calling playsound("the-name-of-the-sound.mp3")`
     - Line 5: `CLEAR = "\033[2J" # clears entire terminal (the program will then print the statement at the bottom of the alarm function)`
     - Line 6: `CLEAR_AND_RETURN = "\033[H" # then this will clear the terminal and return the function again, printing over the previous function output`
     - Line 13: `time.sleep(1) # makes the program wait for 1 second. without it the program will run as fast as the computer can run it`
     - Line 17: `minutes_left = time_left // 60 # indeger division(e.g: 125 // 60 = 2 because 60 evenly divides 125 two times)`
     - Line 18: `seconds_left = time_left % 60 # the remainder after division (e.g: 125 % 6 = 5)`
     - Line 20: `print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")`
     - Line 21: `# :02d = make this number a 2 digits number and add a leading 0 if it's not 2 digits already`

2. **Inline comments (E261)**:

   - The following inline comments should have at least two spaces before the comment to conform to PEP 8:
     - Line 5
     - Line 6
     - Line 13
     - Line 14
     - Line 17
     - Line 18

3. **Blank lines (E302 and E305)**:

   - **E302**: Expected 2 blank lines before a function definition (Line 8).
   - **E305**: Expected 2 blank lines after class or function definition, found 1 (Line 25).

4. **Trailing whitespace (W291)**:

   - Line 13: There's trailing whitespace at the end of the line.

5. **Blank line at end of file (W391)**:
   - Line 31: Blank line at the end of the file should be removed or added as needed.

### Suggested Fixes:

```python
from playsound import playsound
import time

# Function that allows us to play the sound by simply calling playsound("the-name-of-the-sound.mp3")
CLEAR = "\033[2J"  # Clears entire terminal
# (the program will then print the statement at the bottom of the alarm function)
CLEAR_AND_RETURN = "\033[H"  # Clears the terminal and returns the function again,
# printing over the previous function output

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)  # Makes the program wait for 1 second. Without it, the program
        # will run as fast as the computer can run it
        time_elapsed += 1  # Adds 1 second after every loop

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # Integer division (e.g: 125 // 60 = 2
        # because 60 evenly divides 125 two times)
        seconds_left = time_left % 60  # The remainder after division (e.g: 125 % 60 = 5)

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: "
              f"{minutes_left:02d}:{seconds_left:02d}")
        # :02d = make this number a 2 digits number and add a leading 0 if it's not 2 digits already

    playsound("alarm-sound.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
```
