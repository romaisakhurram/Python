import time

def count_down_timer(seconds):
  while seconds > 0:
    mins , secs = divmod(seconds,60)
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer,end="\r")
    time.sleep(1)
    seconds -= 1
  print("00:00 \n Time it's up!")

try:
  total_seconds = int(input("Enter time in seconds and minutes:"))
  count_down_timer(total_seconds)
except ValueError:
    print("Invalid input. Please enter a valid number")

  