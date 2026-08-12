import time
import winsound

alarm_time = input("Enter alarm time (HH:MM): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M")

    if current_time == alarm_time:
        print("⏰ ALARM! Wake up!")
        winsound.Beep(1000, 1000)
        break

    time.sleep(1)
