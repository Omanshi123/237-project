import time
from plyer import notification

def remind_to_drink_water():
    while True:
        notification.notify(
            title='Hydration Reminder',
            message='Time to drink water!',
            timeout=10
        )
        time.sleep(1800)

if __name__ == "__main__":
    remind_to_drink_water()