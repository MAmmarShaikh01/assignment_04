import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# Taking input from user
try:
    user_input = int(input("Enter the countdown time in seconds: "))
    countdown_timer(user_input)
except ValueError:
    print("Please enter a valid number.")
