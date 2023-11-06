import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="please drink water now",
            message="Getting enough water every day is important for your health",
            timeout=5

        )
        time.sleep(6)


