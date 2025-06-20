import datetime
import time
import os

def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("Wake up! Alarm ringing!")
            # You can replace this with a sound if desired
            for i in range(5):
                print("🔔 Alarm 🔔")
                time.sleep(1)
            break
        time.sleep(1)

# Example Usage
alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")
alarm_clock(alarm_time)
